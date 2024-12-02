package org.aoc.model.year2024;

import org.aoc.model.Solution;

import java.util.ArrayList;

public class D1P2 extends Solution {
    public D1P2() {
        super(2024, 1, 2);
    }

    public int countOccurences(ArrayList<Integer> l, int i) {
        int count=0;
        for (Integer j: l) {
            if (j.equals(i)) {
                count++;
            }
        }
        return count;
    }

    @Override
    public Object run() {
        ArrayList<Integer> left = new ArrayList<>();
        ArrayList<Integer> right = new ArrayList<>();

        for (String item: this.txtInput) {
            left.add(Integer.parseInt(item.split("\\s+")[0]));
            right.add(Integer.parseInt(item.split("\\s+")[1]));
        }

        int similiarityScore = 0;
        for (Integer i: left) {
            similiarityScore = similiarityScore + (i * countOccurences(right, i));
        }
        return similiarityScore;
    }
}
