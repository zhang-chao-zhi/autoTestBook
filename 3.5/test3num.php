<?php

class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer[][]
     */
    function threeSum($nums) {
        $count = count($nums);
        $result = [];
        for ($i =0; $i < $count - 2; $i++) {
            $first = $nums[$i];
            for ($j = $i + 1; $j < $count -1;$j++) {
             for ($k = $j+1; $k < $count; $k++) {
                 if ($nums[$i] + $nums[$j] + $nums[$k] == 0) {
                     $result[] = [$nums[$i], $nums[$j], $nums[$k]];
                 }
             }
            }
        }

        return $result;
    }
}


$s = new Solution();

$result = $s->threeSum([-1,0,1,2,-1,-4]);
var_dump($result);