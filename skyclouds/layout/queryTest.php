<?php
    function writeMsg($query) {
        require_once 'php/conn.php';
        $conn = new mysqli($hn, $un, $pw, $db);
        if ($conn->connect_error) die($conn->connect_error);
        echo "Hello world!";
        $result = $conn->query($query);
        if (!result) die("Database access failed: " . $conn->error);

        echo <<<_END
            <script language="JavaScript">
                var gauge1 = loadLiquidFillGauge("fillgauge1", $result);
            </script>
_END;
    

        $result->close();
        $conn->close();

        function get_post($conn, $var)
        {
            return $conn->real_escape_string($_POST[$var]);
        }
    }
    ?>