package org.aoc.model;

public class DynamicArray {
    private int[] array;
    private int capacity;
    private int size;

    public DynamicArray(int capacity) {
        this.array = new int[capacity];
        this.capacity = capacity;
        this.size = 0;
    }

    public boolean isFull() {
        return this.getSize() == this.getCapacity();
    }

    public int get(int i) {
        return this.array[i];
    }

    public void set(int i, int n) {
        this.array[i] = n;
    }

    public void extend(int n) {
        DynamicArray newArray = new DynamicArray(n);
        int counter = 0;
        for (int i : this.array) {
            newArray.set(counter, i);
            counter++;
        }
        this.array = newArray.array;
        this.capacity = n;
        this.size = counter;
    }

    public void pushback(int n) {
        if (this.isFull()) {
            this.resize();
        }
        this.set(this.getSize(), n);
        this.size++;
    }

    public int popback() {
        int val = this.get(this.getSize() - 1); // The last element
        DynamicArray newArray = new DynamicArray(this.getSize());
        for (int i = 0; i < this.getSize() - 1; i++) {
            newArray.set(i, this.get(i));
        }
        this.array = newArray.array;
        this.size--;
        return val;
    }

    private void resize() {
        this.extend(this.getCapacity() * 2);
    }

    public int getSize() {
        return this.size;
    }

    public int getCapacity() {
        return this.capacity;
    }
}