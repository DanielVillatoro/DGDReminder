var btnNotificacion = document.getElementById("buttonN"),  
    btnPermiso = document.getElementById("buttonP")
    titulo = "Fili Santill�n",
    opciones = {
        icon: "logo.png",
        body: "Notificaci�n de prueba"
    };

function permiso() {  
        Notification.requestPermission();
};

function mostrarNotificacion() {  
    if(Notification) {
        if (Notification.permission == "granted") {
            var n = new Notification(titulo, opciones);
        }

        else if(Notification.permission == "default") {
            alert("Primero da los permisos de notificaci�n");
        }

        else {
            alert("Bloqueaste los permisos de notificaci�n");
        }
    }
};

btnPermiso.addEventListener("click", permiso);  
btnNotificacion.addEventListener("click", mostrarNotificacion);