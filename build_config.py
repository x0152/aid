MAIN_SERIVCE = "./vendor/serviceControl"
TEMPLATE_CONFIG = "./vendor/serviceControl/templates/templateConfig.conf"

SERVICES =  {"./vendor/serviceAccess" : 
            {
              "Name": "Access",
              "Cmd": "serviceAccess",
              "Port": 4343,
              "Version": "1.00",
              "IsHttpInterface" : True,
              "IsAutoload" : True 
            },

            "./vendor/serviceDeliveryFiles" : 
            {
              "Name": "Devlivery-files",
              "Cmd": "serviceDeliveryFiles",
              "Port": 9000,
              "Version": "1.00",
              "IsHttpInterface" : True,
              "IsAutoload" : True 
            },

            "./vendor/serviceManagerLogs" :  
            {
              "Name": "Manager-logs",
              "Cmd": "serviceManagerLogs",
              "Port": 9001,
              "Version": "1.00",
              "IsHttpInterface" : True,
              "IsAutoload" : True 
            },

            "./vendor/serviceNetcat" : 
            {
              "Name": "Web-Netcat",
              "Cmd": "serviceNetcat",
              "Port": 9002,
              "Version": "1.00",
              "IsHttpInterface" : True,
              "IsAutoload" : True 
            },


            "./vendor/serviceNotification" : 
            {
              "Name": "Notification",
              "Cmd": "serviceNotification",
              "Port": 2323,
              "Version": "1.00",
              "IsHttpInterface" : False,
              "IsAutoload" : False 
            },



            "./vendor/servicePythonScripts" :  
            {
              "Name": "Python-scripts",
              "Cmd": "servicePythonScripts",
              "Port": 9003,
              "Version": "1.00",
              "IsHttpInterface" : True,
              "IsAutoload" : True 
            },


            "./vendor/serviceReceptionFiles" :  
            {
              "Name": "Reception-files",
              "Cmd": "serviceReceptionFiles",
              "Port": 9004, 
              "Version": "1.00",
              "IsHttpInterface" : True,
              "IsAutoload" : True
            }}

