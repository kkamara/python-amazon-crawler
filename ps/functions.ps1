
function Invoke-DockerSetup {
    docker-compose up --build
}

function Remove-DockerSetup {
    docker-compose down
}
