. "$pwd\ps\functions"

switch($args[0]) {
    start {
        Invoke-DockerSetup
    }
    stop {
        Remove-DockerSetup
    }
    default {}
}
