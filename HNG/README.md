DevOps Internship at HNG!🚀

# Nginx Installation and Configuration 🚀

During my DevOps internship, I had the opportunity to work on installing and configuring Nginx, a high-performance web server and reverse proxy server. Here’s a quick overview of the steps I followed and key insights I gained!

<strong> 🔧 Approach:</strong>

- Installation: I started by installing Nginx on a Ubuntu server using apt-get for easy installation:

`sudo apt update`
`sudo apt install nginx`

- Starting Nginx: After installation, type `localhost` in your browser. If you are getting <img src="./img1.png"> Yaay! You've successfully installed nginx. 

- Creating HTML page: Still on your terminal, change directory to `/var/www/html` then create an index.html file.

`cd /var/www/html`
`sudo vi index.html`

- Customize the html file to your liking! Here's an example to get you started:
<img src="./img2.png">

- Configuration: Nginx's configuration files are located in /etc/nginx/. Firstly, open anew terminal<em>(Ctrl+Alt+t)</em> then:

`cd /etc/nginx/sites-enabled`
`sudo service nginx restart`
`sudo service nginx status`

- Testing: I tested the installation by accessing the server’s public IP address in a browser e.g `http://192.168.235.233/`


<strong> 💡 Challenges and Solutions:</strong>

One of the key challenges I faced was while navigating the directories for Nginx configuration, I ran into a problem where the symbolic link wasn’t behaving as expected. When I tried to cd into the /etc/nginx/sites-available/default directory, I received the error:


<strong> 🌱 Learning and Professional Growth:</strong>

This task contributed significantly to my learning in DevOps. It enhanced my understanding of web server management, network configurations, and security practices. Nginx, being lightweight and highly customizable, gave me valuable experience in configuring scalable and reliable systems.

As I continue my journey, I see how mastering tools like Nginx aligns with my goals of becoming proficient in the full DevOps lifecycle—ensuring smooth deployment, system stability, and security.

🔗 For more insights on DevOps and hiring DevOps engineers, check out this <a href="https://hng.tech/hire/devops-engineers">resource</a>. Wait! <a href="https://hng.tech/hire/automation-engineers">Automation Engineers?</a> I gatchu still! 😊
