<?php
include ('includes/dbconnection.php');
session_start();
error_reporting(0);
include ('includes/dbconnection.php');

if (isset($_POST['submit'])) {
    $name = $_POST['name'];
    $email = $_POST['email'];
    $phone = $_POST['phone'];


    // Form validation
    $errors = array();

    if (empty($name)) {
        $errors[] = "Name is required.";
    }

    if (empty($email)) {
        $errors[] = "Email is required.";
    } elseif (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        $errors[] = "Invalid email format.";
    }

    if (empty($phone)) {
        $errors[] = "Phone number is required.";
    } elseif (!preg_match('/^[0-9]{10}$/', $phone)) {
        $errors[] = "Invalid phone number format. Please enter a 10-digit number.";
    }

    if (empty($services)) {
        $errors[] = "Please select a service.";
    }

    if (empty($adate)) {
        $errors[] = "Appointment date is required.";
    }

    if (empty($atime)) {
        $errors[] = "Appointment time is required.";
    }

    if (empty($errors)) {
        $_SESSION['name'] = $name;
        $_SESSION['email'] = $email;
        $_SESSION['services'] = $services;
        $_SESSION['adate'] = $adate;
        $_SESSION['atime'] = $atime;
        $_SESSION['phone'] = $phone;
        $_SESSION['aptnumber'] = $aptnumber;

        $query = mysqli_query($con, "SELECT * FROM user_table WHERE name = '$name' AND  = '$atime'");
        if (mysqli_num_rows($query) > 0) {
            echo "<script>alert('The selected time is already booked. Please choose a different time.');</script>";
        } else {
            $query = mysqli_query($con, "INSERT INTO tblappointment(AptNumber, Name, Email, PhoneNumber, AptDate, AptTime, Services) VALUES ('$aptnumber','$name','$email','$phone','$adate','$atime','$services')");
            if ($query) {
                echo "<script>window.location.href='payment_gateaway.php'</script>";
                exit();
            } else {
                echo "<script>alert('Something went wrong. Please try again.');</script>";
            }
        }
    }
}
?>