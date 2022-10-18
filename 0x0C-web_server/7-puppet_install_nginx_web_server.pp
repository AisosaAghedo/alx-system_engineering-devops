#Install Nginx web server (w/ Puppet)
package {'nginx':
name     => 'nginx',
provider => 'apt',
ensure   => 'latest',
}
