<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Obtiene los datos del formulario
    $name = strip_tags(trim($_POST["name"]));
    $email = filter_var(trim($_POST["email"]), FILTER_SANITIZE_EMAIL);
    $subject = strip_tags(trim($_POST["subject"]));
    $message = strip_tags(trim($_POST["message"]));

    // Verifica que los campos no estén vacíos y que el email sea válido
    if (empty($name) || empty($subject) || empty($message) || !filter_var($email, FILTER_VALIDATE_EMAIL)) {
        echo "Por favor complete todos los campos correctamente.";
        exit;
    }

    // Configura el destinatario y el asunto
    $to = "lalomoto21@gmail.com"; // Reemplaza con tu correo electrónico
    $email_subject = "Nuevo mensaje de: $name - $subject";

    // Construye el contenido del correo electrónico
    $email_body = "Nombre: $name\n";
    $email_body .= "Correo: $email\n\n";
    $email_body .= "Mensaje:\n$message\n";

    // Configura los encabezados
    $headers = "From: $name <$email>";

    // Envía el correo electrónico y verifica el resultado
    if (mail($to, $email_subject, $email_body, $headers)) {
        echo "success";
    } else {
        echo "Error al enviar el mensaje. Inténtelo de nuevo.";
    }
}
?>"
