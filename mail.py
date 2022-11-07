from mailer import Mailer

mail = Mailer("erricmullar.neutron@gmail.com",
              "akshay2005")

mail.send("akshay.vs2005.com",  # Email From Any service Provider
          "noreplay@example.com", # Redirect receiver to another email when try to reply.
          )