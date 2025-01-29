DevOps Internship at HNG!🚀

# Nginx Installation and Configuration 🚀

During my DevOps internship, I had the opportunity to work on installing and configuring Nginx, a high-performance web server and reverse proxy server. Here’s a quick overview of the steps I followed and key insights I gained!

<strong> 🔧 Approach:</strong>

- Installation: I started by installing Nginx on a Ubuntu server using apt-get for easy installation:

`sudo apt update`

`sudo apt install nginx`

- Starting Nginx: After installation, type `localhost` in your browser. If you are getting:
 <img src="./img1.png"> 

 <em>Yaay! You've successfully installed nginx.</em>

- Creating HTML page: Still on your terminal, change directory to `/var/www/html` then create an index.html file.

`cd /var/www/html`

`sudo vi index.html`

- Customize the html file to your liking! Here's an example to get you started:
<img src="./img2.png">

- Configuration: Nginx's configuration files are located in /etc/nginx/. Firstly, open a new terminal<em>(Ctrl+Alt+t)</em> then:

`cd /etc/nginx/sites-enabled`

`sudo service nginx restart`

`sudo service nginx status`

- Testing: I tested the installation by accessing the server’s public IP address in a browser e.g `http://192.168.235.233/`


<strong> 💡 Challenges and Solutions:</strong>
🔴 Issue: Symbolic Link & Accessing Default File.

While configuring Nginx, I ran into a symbolic link issue that prevented me from accessing the default configuration file. At first, I thought default was a directory:

<img src="./img3.png">

However, when I tried to navigate into /etc/nginx/sites-available/default, I got the following error:
<img src="./img4.png">

The same issue occurred when I tried to cd into default directly:
<img src="./img5.png">

After investigating, I realized that default wasn't a directory but a plain configuration file. The correct way to interact with it was by opening it with a text editor like vim:
<img src="./img6.png">

I also checked if the symbolic link in /etc/nginx/sites-enabled/ was properly pointing to this file:
<img src="./img7.png">


If the link was missing or broken, I recreated it using:

`sudo ln -s /etc/nginx/sites-available/default /etc/nginx/sites-enabled/`


<strong> 🌱 Learning and Professional Growth:</strong>

This task contributed significantly to my learning in DevOps. It enhanced my understanding of web server management, network configurations, and security practices. Nginx, being lightweight and highly customizable, gave me valuable experience in configuring scalable and reliable systems.

As I continue my journey, I see how mastering tools like Nginx aligns with my goals of becoming proficient in the full DevOps lifecycle—ensuring smooth deployment, system stability, and security.

🔗 Hiring skilled DevOps engineers? Check out this <a href="https://hng.tech/hire/devops-engineers">resource</a>. Oh, and if you’re looking for Automation Engineers <a href="https://hng.tech/hire/automation-engineers">click here.</a> Thank you for your time! 😊
