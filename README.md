# Django
## Step 1 For Graphite and Grafana
# Tried installing graphite using following link 
https://www.vultr.com/docs/how-to-install-and-configure-graphite-on-ubuntu-16-04
But it didn't work

# For Grafana installation
https://grafana.com/docs/installation/debian/
Worked!

After these two you need to start apache server
Installed apache with the following command
```
sudo apt-get install apache2 libapache2-mod-wsgi -y
```
Copying graphite configuration file to apache
```
sudo cp /usr/share/graphite-web/apache2-graphite.conf /etc/apache2/sites-available/
sudo a2dissite 000-default
sudo a2ensite apache2-graphite
```
After that my nginx was running on port 80 I had to kill it using
```
ps -eaf | grep nginx
sudo kill -9 1764
```
See if any process still running
```
sudo netstat -tulpn | grep :80
```
Restart the apache2 
```
sudo systemctl restart apache2
```
Nothing above was useful
Used docker instead:
Used the following link
https://graphite.readthedocs.io/en/latest/install.html#docker
Ran the following code:
```
docker run -d\
 --name graphite\
 --restart=always\
 -p 80:80\
 -p 2003-2004:2003-2004\
 -p 2023-2024:2023-2024\
 -p 8125:8125/udp\
 -p 8126:8126\
 graphiteapp/graphite-statsd
 ```
 Used following handy commands:
 To delete the docker created
 ```
 docker system prune
 ```
 It ran after some time, maybe docker takes time to start.
 
 # Step 2
 Graphite is up running.
 You can see a memUsage file.
 Graphite does read the data, we have to feed it.
 ```
 echo "test.count 4 `date +%s`" | nc -q0 127.0.0.1 2003
 ```
Metric messages need to contain a metric name, a value, and a timestamp. We can do this in our terminal. Let's create a value that will match our test storage schema that we created. We will also match one of the definitions that will add up the values when it aggregates. We'll use the date command to make our timestamp.

# Step 3
if we want relational database to use.
We change the ini file of grafana
which is at
```
/etc/grafana/grafana.ini
```
First, keep in mind that Graphite-web supports Python versions 2.6 to 2.7 and Django versions 1.4 and above.

# Step 4
We want to send the metric to the graphite server, use graphitesend
```
import graphitesend
g = graphitesend.init(prefix='test', system_name='', graphite_server='127.0.0.1')
g.send('count', 10)
```

# links used
https://www.vultr.com/docs/how-to-install-and-configure-graphite-on-ubuntu-16-04
https://www.digitalocean.com/community/tutorials/how-to-install-and-use-graphite-on-an-ubuntu-14-04-server
https://www.digitalocean.com/community/tutorials/an-introduction-to-tracking-statistics-with-graphite-statsd-and-collectd
https://grafana.com/docs/installation/configuration/
https://matt.aimonetti.net/posts/2013/06/26/practical-guide-to-graphite-monitoring/
https://play.grafana.org/d/000000012/grafana-play-home?orgId=1

# Installation of Graphite on aws
1. Install docker
```
sudo apt install docker.io
```
2. Run docker command
```
docker run -d\
 --name graphite\
 --restart=always\
 -p 80:80\
 -p 2003-2004:2003-2004\
 -p 2023-2024:2023-2024\
 -p 8125:8125/udp\
 -p 8126:8126\
 graphiteapp/graphite-statsd
 ```
 It may happen that someone using a port
 To check the port
 ```
 sudo netstat -tulpn | grep :2004
 ps -eaf | grep 31123
 ```
 Try to make sure no one is running on the ports mentioned in docker command
 
3. Run for Graphite
```
http://ec2-52-26-169-20.us-west-2.compute.amazonaws.com:80
```
Done!

# Installation of Grafana
1. You have to open the port 3000 for EC2 instance.
```
sudo add-apt-repository "deb https://packages.grafana.com/oss/deb stable main"
curl https://packages.grafana.com/gpg.key | sudo apt-key add -
sudo apt-get update
sudo apt-get install grafana
```

2. Run the grafana
```
sudo service grafana-server start
```
