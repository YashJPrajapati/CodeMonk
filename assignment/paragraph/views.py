# Django imports
from django.shortcuts import render, redirect  # For rendering templates and redirecting user requests
from django.conf import settings  # For accessing Django settings
from django.views.decorators.csrf import csrf_exempt  # For exempting CSRF protection for specific views
from django.utils import timezone

# Third-party imports
from rest_framework.parsers import FileUploadParser  # For parsing file uploads in API views
from rest_framework.response import Response  # For constructing HTTP responses in API views
from rest_framework.views import APIView  # For creating API views
from rest_framework import status  # For HTTP status codes in API responses

# Standard library imports
import datetime  # For working with date and time
import smtplib  # For sending emails
from email.message import EmailMessage  # For creating email messages
import jwt  # For encoding and decoding JSON Web Tokens (JWT)
import os  # For interacting with the operating system

# Local imports
from .utils import *  # Importing utility functions0
from .models import *  # Importing Django models
from .serializers import *  # Importing serializers for Django models



# API view for user signup
class signup(APIView):
    def post(self, request):
        # Extract data from the request
        email = request.data.get("Email")
        name = request.data.get("name")
        dob = request.data.get("dob(YYYY-MM-DD)")
        
        # Encode the payload including the expiration time
        Token = jwt.encode({'Email': email, 'name': name}, 'secret_key', algorithm='HS256')
        
        # Generate a random OTP
        Otp = generate_otp()
        subject = 'Registration Details'
        email_body = f"""Dear User,

        Your One-Time Password (OTP) is: {Otp}
        Your Token To Be Used While Login Is: {Token}

        Thank you for Registration. Your Account Was Created Successfully.
        Regards,
        Yash Prajapati
        (+91) 94265-56709
        yashprajapati2017@gmail.com
        """
        # Create user data
        user_data = {
            "email": email,
            "name": name,
            "dob": dob,
            "Token": Token,
            "Otp": Otp,
        }

        # Send registration email and save user data
        send_email_func(email_body, subject, email)
        Login.objects.create(**user_data)

        # Redirect to signin page after successful registration
        return redirect('signin')

# Decorator for CSRF exemption for sending emails
@csrf_exempt    
def send_email_func(email_body, subject, email):
    msg = EmailMessage()
    msg.set_content(email_body)  # Set the content directly
    msg['Subject'] = subject
    msg['From'] = "CodeMonk TEAM <settings.EMAIL_HOST_USER> "
    msg['To'] = email

    # Connect to SMTP server and send email
    server = smtplib.SMTP_SSL(settings.EMAIL_HOST, settings.EMAIL_PORT)
    server.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)
    server.send_message(msg)
    
    server.quit()

# API view for user signin
class signin(APIView):
    def post(self, request):
        # Extract signin data from the request
        email = request.data.get("Email")
        Token = request.data.get("Token")
        Otp = request.data.get("Otp")
        request.session['Email'] = email
        
        # Check if all required fields are provided
        if not (email or Token or Otp):
            return Response({"Error 404": "All Fields are Mandatory"}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            # Retrieve user data from the database
            user = Login.objects.get(email=email)
            
            # Validate token and OTP
            if Token == user.Token and Otp == user.Otp:
                user.status = True
                user.save()
                return redirect('para')  # Redirect to paragraph API endpoint after successful signin
            else:
                return Response({"Error": "Invalid token or Otp"}, status=status.HTTP_401_UNAUTHORIZED)

        # Handle exceptions
        except Login.DoesNotExist:
            return Response({"Error 404": "User Not Found", "For Login Id": email})
        except jwt.ExpiredSignatureError:
            return Response({"Message": "Token has expired"}, status=status.HTTP_401_UNAUTHORIZED)
        except jwt.InvalidTokenError:
            return Response({"Message": "Invalid token"}, status=status.HTTP_401_UNAUTHORIZED)

# API view for user signout
class signout(APIView):
    def get(self, request):
        try:
            # Check if any user is logged in
            if Login.objects.filter(status=True).exists():
                email = request.session.get('Email')
                if email:
                    try:
                        user = Login.objects.get(Email=email)
                        if user.status:
                            user.status = False
                            user.save()
                            return Response({"Message": "Logout Successful"}, status=status.HTTP_200_OK)
                        else:
                            return Response({"Message": "User is already logged out"}, status=status.HTTP_200_OK)
                    except Login.DoesNotExist:
                        return Response({"Error": "User Not Found"}, status=status.HTTP_404_NOT_FOUND)
            else:
                return Response({"Error": "Please Login First"}, status=status.HTTP_401_UNAUTHORIZED)
                
        except Login.DoesNotExist:
            return Response({"Error": "Access Denied"}, status=status.HTTP_404_NOT_FOUND)

# API view for creating and indexing paragraphs
class ParagraphAPI(APIView):
    def post(self, request):
        try:
            if Login.objects.get(status=True):
                data = request.data  # Get the request data

                if isinstance(data, list):  # Check if data is a list
                    indexed_paragraphs = []  # List to store indexed paragraphs
                    word_paragraph_mapping = {}  # Dictionary to store mapping of words to paragraph IDs

                    for index, item in enumerate(data, start=1):
                        content = item.get('content', '')  # Get the content from each item

                        if content:
                            paragraphs = content.split('\n')  # Split content into separate paragraphs based on newline characters

                            for paragraph_content in paragraphs:
                                # Create a new paragraph instance without explicitly setting the ID
                                paragraph = Paragraph.objects.create(content=paragraph_content)

                                # Tokenize words by splitting at whitespace and convert to lowercase
                                words = paragraph_content.lower().split()

                                # Index words against the paragraph they are from
                                for word in words:
                                    if word in word_paragraph_mapping:
                                        word_paragraph_mapping[word].append(paragraph.id)
                                    else:
                                        word_paragraph_mapping[word] = [paragraph.id]

                                indexed_paragraphs.append({'id': paragraph.id, 'content': paragraph_content})

                    return Response({'message': 'Paragraphs created and indexed successfully', 'paragraphs': indexed_paragraphs, 'word_paragraph_mapping': word_paragraph_mapping}, status=status.HTTP_201_CREATED)
                else:
                    return Response({'error': 'Data should be a list of JSON objects'}, status=status.HTTP_400_BAD_REQUEST)
        except Login.DoesNotExist:
            return Response({"Error": "Access Denied"}, status=status.HTTP_404_NOT_FOUND)
        except Login.MultipleObjectsReturned:
            return Response({"Error": "Multiple active users found"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# API view for creating and indexing paragraphs (alternative implementation)
class Createwithlist(APIView):
    def post(self, request):
        try:
            if Login.objects.get(status=True):
                data = request.data  # Get the request data

                if isinstance(data, list):  # Check if data is a list
                    indexed_paragraphs = []  # List to store indexed paragraphs
                    word_paragraph_mapping = {}  # Dictionary to store mapping of words to paragraph IDs

                    for index, paragraph_content in enumerate(data, start=1):
                        # Create a new paragraph instance without explicitly setting the ID
                        paragraph = Paragraph.objects.create(content=paragraph_content)

                        # Tokenize words by splitting at whitespace and convert to lowercase
                        words = paragraph_content.lower().split()

                        # Index words against the paragraph they are from
                        for word in words:
                            if word in word_paragraph_mapping:
                                word_paragraph_mapping[word].append(paragraph.id)
                            else:
                                word_paragraph_mapping[word] = [paragraph.id]

                        indexed_paragraphs.append({'id': paragraph.id, 'content': paragraph_content})

                    return Response({'message': 'Paragraphs created and indexed successfully', 'paragraphs': indexed_paragraphs, 'word_paragraph_mapping': word_paragraph_mapping}, status=status.HTTP_201_CREATED)
                else:
                    return Response({'error': 'Data should be a list of JSON objects'}, status=status.HTTP_400_BAD_REQUEST)
        except Login.DoesNotExist:
            return Response({"Error": "Access Denied"}, status=status.HTTP_404_NOT_FOUND)
        except Login.MultipleObjectsReturned:
            return Response({"Error": "Multiple active users found"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# API view for creating and indexing paragraphs from a file
class Createwithfile(APIView):
    parser_class = (FileUploadParser,)

    def post(self, request, *args, **kwargs):
        try:
            if Login.objects.get(status=True):
                file_obj = request.FILES.get('file', None)
                if file_obj:
                    paragraphs = []
                    word_paragraph_mapping = {}

                    # Read the file line by line
                    for index, line in enumerate(file_obj):
                        line = line.decode('utf-8').strip()  # Decode byte string to Unicode and strip leading/trailing whitespaces
                        
                        if line:  # Check if the line is not empty
                            # Create a new paragraph instance
                            paragraph = Paragraph.objects.create(content=line)

                            # Tokenize words by splitting at whitespace and convert to lowercase
                            words = line.lower().split()

                            # Index words against the paragraph they are from
                            for word in words:
                                if word in word_paragraph_mapping:
                                    word_paragraph_mapping[word].append(paragraph.id)
                                else:
                                    word_paragraph_mapping[word] = [paragraph.id]

                            paragraphs.append({'id': paragraph.id, 'content': line})

                    return Response({'message': 'Paragraphs created and indexed successfully', 'paragraphs': paragraphs, 'word_paragraph_mapping': word_paragraph_mapping}, status=status.HTTP_201_CREATED)
                else:
                    return Response({'error': 'No file was uploaded'}, status=status.HTTP_400_BAD_REQUEST)
        except Login.DoesNotExist:
            return Response({"Error": "Access Denied"}, status=status.HTTP_404_NOT_FOUND)
        except Login.MultipleObjectsReturned:
            return Response({"Error": "Multiple active users found"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# API view for searching paragraphs
class SearchAPI(APIView):
    def get(self, request):
        try:
            if Login.objects.get(status=True):
                search_word = request.data.get("search_word")
                if search_word:
                    search_word = search_word.lower().strip()
                    paragraphs = Paragraph.objects.filter(content__icontains=search_word)[:10]
                    results = []
                    for paragraph in paragraphs:
                        words = paragraph.content.lower().split()
                        if search_word in words:
                            results.append({'paragraph_id': paragraph.id, 'paragraph_content': paragraph.content})
                    return Response(results, status=status.HTTP_200_OK)
                else:
                    return Response({'error': 'Search word is required'}, status=status.HTTP_400_BAD_REQUEST)
        except Login.DoesNotExist:
            return Response({"Error": "Access Denied"}, status=status.HTTP_404_NOT_FOUND)
        except Login.MultipleObjectsReturned:
            return Response({"Error": "Multiple active users found"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class Modifyuser(APIView):
    def post(self, request):
        email = request.data.get("Email")
        job = request.data.get("dob(YYYY-MM-DD)")

        # Check if email exists in the database
        try:
            user = Login.objects.get(email=email)
        except Login.DoesNotExist:
            return Response({"message": "User with this email does not exist"}, status=status.HTTP_404_NOT_FOUND)

        # Generate a new token
        modifiedAt = timezone.now()
        new_token = jwt.encode({'Email': email, 'mod': modifiedAt.isoformat()}, 'secret_key', algorithm='HS256')

        # Generate a new OTP
        new_otp = generate_otp()

        # Update user's token and OTP in the database
        user.Token = new_token
        user.Otp = new_otp
        user.modifiedAt = modifiedAt
        user.save()

        # Send email with new OTP
        subject = 'Login Credential Regeneration Details'
        email_body = f"""Dear User,

        Your One-Time Password (OTP) for token regeneration is: {new_otp}
        Your New Token: {new_token}

        Regards,
        Your App Team
        """
        send_email_func(email_body, subject, email)

        return Response({"message": "Token and OTP regenerated successfully"}, status=status.HTTP_200_OK)
