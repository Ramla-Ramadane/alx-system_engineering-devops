# find the issue
exec { 'killmenow':
    command => "sed -i 's/class-wp-locale.phpp/class-wp-locale.php/g' /var/www/html/wp-settings.php",
    path    => '/bin',
}
