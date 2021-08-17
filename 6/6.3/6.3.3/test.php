<?php 
$array = [1, 2, 3, 4];
array_walk($array, function(&$value) {$value = $value * $value;});
var_dump($array);
