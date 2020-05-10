Exercise 07
1. Create a python program that reads apache log file - access_log and from that log file using regular expressions extracts and group following information:

- IP address 

- accessed page path 



And based on that information:

 - show top 5 IP addresses based on the count of connections

  - show top 5 most vissited web content  



Sample log file format: 

128.227.88.79 - - [08/Mar/2004:06:57:46 -0800] "GET /twiki/bin/view/Main/WebHome HTTP/1.1" 200 10419

128.227.88.79 - - [08/Mar/2004:06:57:46 -0800] "GET /twiki/pub/TWiki/TWikiLogos/twikiRobot46x50.gif HTTP/1.1" 304 -

64.242.88.10 - - [08/Mar/2004:07:00:15 -0800] "GET /twiki/bin/view/TWiki/DontNotify?rev=1.1 HTTP/1.1" 200 3965

64.242.88.10 - - [08/Mar/2004:07:07:13 -0800] "GET /twiki/bin/edit/Main/Masquerade_classes?topicparent=Main.ConfigurationVariables HTTP/1.1" 401 12846

2. From the apache error_log file extract error messages and show report

- clacify the type of error 

- when the error had happend 

- which user IP addresses has been affected 
