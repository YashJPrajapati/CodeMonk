# Sample input For all the APIs:

* signup API:
```shell
  {
    "Email": "example@example.com",
    "name": "John Doe",
    "dob(YYYY-MM-DD)": "1990-01-01"
  }
```
* signin API: (Will Rechive otp and token on email will creating the user on signup api)
```shell
  {
    "Email": "example@example.com",
    "Token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJFbWFpbCI6ImV4YW1wbGVAZXhhbXBsZS5jb20iLCJuYW1lIjoiSm9obiBEb2UiLCJpYXQiOjE1MTYyMzkwMjIsImV4cCI6MTUxNjIzOTEyMn0.jG1dHAAwGOC06iEjNCJ6HwvweV7Lo91Jc7lpg_h8Rxw",
    "Otp": "123456"
  }
```

* Modifyuser API:
```shell
  {
    "Email": "example@example.com",
    "dob(YYYY-MM-DD)": "1990-01-01"
  }
```

* ParagraphAPI: (For Multiple Input using List Formate)
```shell
  [
    {
      "content": "This is the first paragraph."
    },
    {
      "content": "This is the second paragraph."
    }
  ]
```

* Createwithlist API: (Alternate Way for Cadd Paragraph)
```shell
  [
    "This is the first paragraph.",
    "This is the second paragraph."
  ]
```

* SearchAPI:
```shell
  {
    "search_word": "paragraph"
  }
```
