# server-client
 
This is a blocking server-client application with socket programming.

In order to run the program, after you download/pull the code : 
<ol>
 <li>open a terminal, type "python3 server.py". You have to see a prompt for server starts listening for a socket.</li>
 <li>open another/different terminal, type "python3 client.py". You have to see a prompt for client's connection to server.</li>
 <li>after you run the command in client terminal, switch back to terminal you started server. You have to see a prompt for datasae connection and its proper operations</li>
<ol>
 
I ran the program <b>venv</b> environment with python 3.11. You should not be encountered any problems besides some OS/Blocking problems.I fyou encounter any other problems related than OS/Blocking problems, then probably your environment or python version are incompatible.

I try to handle as many exceptions as possible. But of course there has to some that I missed. This server is for blocking connection, which means it will block or raise some errors when you try to reach to server from multiple clients.

So this server can be improved with a non-blocking server and client
