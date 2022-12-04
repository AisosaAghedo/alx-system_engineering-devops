Issue Summary:

Upon the release of ALX's System Engineering & DevOps project 0x19, approximately 18:00 West African Time (WAT) on the 31st of November,2022, an outage occurred on an isolated Ubuntu 14.04 container running an Apache web server. GET requests on the server led to 500 Internal Server Error's, when the expected response was an HTML file defining a simple Holberton WordPress site.
The WordPress app was encountering a critical error in wp-settings.php when trying to load the file class-wp-locale.phpp. The correct file name, located in the wp-content directory of the application folder, was class-wp-locale.php.

Patch involved a simple fix on the typo, removing the trailing p.

Timeline, Root cause and resolution:

I encountered the issue upon opening the project at roughly 18:30 WAT and promptly proceeded to undergo solving the problem.

Checked running processes using ps aux. Two apache2 processes - root and www-data - were properly running.

Looked in the sites-available folder of the /etc/apache2/ directory. Determined that the web server was serving content located in /var/www/html/.

In one terminal, ran strace on the PID of the root Apache process. In another, curled the server , strace gave no useful information.

Repeated the previous step, except on the PID of the www-data process, strace revelead an -1 ENOENT (No such file or directory) error occurring upon an attempt to access the file /var/www/html/wp-includes/class-wp-locale.phpp.

Looked through files in the /var/www/html/ directory one-by-one, using Vim pattern matching to try and locate the erroneous .phpp file extension. Located it in the wp-settings.php file.

Removed the trailing p

Tested another curl on the server and received status code 200

Wrote a Puppet manifest to automate fixing of the error.

Corrective and Preventative measures:

This outage was not a web server error, but an application error. To prevent such outages moving forward, the following things should be done:

 Test the application before deploying. This error would have arisen and could have been addressed earlier had the app been tested.

 Status monitoring. Enable some uptime-monitoring service such as UptimeRobot to alert instantly upon outage of the website.

In response to this error, a Puppet manifest 0-strace_is_your_friend.pp was written to automate fixing of any such identitical errors should they occur in the future. The manifest replaces any phpp extensions in the file /var/www/html/wp-settings.php with php.
