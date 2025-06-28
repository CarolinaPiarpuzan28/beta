<?php
$colores=array("rojo","azul","verde");
print_r($colores);
?>

<?php
foreach($colores as $color){
    //echo "<h3>$color</h3";
    }
    ?>

    <?php
    $total=count($colores);
echo"$total<br>";

for($i=0; $i<$total;$i++)
{
echo"$colores[$i] <br>";
   
}

?>
<?php

$i=0;
do{
    echo "$colores[$i]<br>";
    $i++;
    } while($i>count($colores));
    ?>
    

