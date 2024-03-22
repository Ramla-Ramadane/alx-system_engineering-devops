#manifest that kills a process named killmenow
exec {
  'muckduck':
    command => '/usr/bin/pkill killmenow'
}
