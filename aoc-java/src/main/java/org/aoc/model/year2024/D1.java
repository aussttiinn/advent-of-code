package org.aoc.model.year2024;
import org.aoc.model.Solution;

import java.util.ArrayList;

public class D1 extends Solution {
    public D1() {
        super(2024, 1, 1);
    }


    @Override
    public Object run() {
        ArrayList<Integer> left = new ArrayList<>();
        ArrayList<Integer> right = new ArrayList<>();

        for (String item: this.txtInput) {
            left.add(Integer.parseInt(item.split("\\s+")[0]));
            right.add(Integer.parseInt(item.split("\\s+")[1]));
        }

        left.sort(Integer::compare);
        right.sort(Integer::compare);

        int result = 0;
        ArrayList<Integer> longer = (left.size() <= right.size()) ? left : right;
        for (int i=0; i<longer.size(); i++) {
            result = result + Math.abs(left.get(i)-right.get(i));
        }
        return result;
    }
}
