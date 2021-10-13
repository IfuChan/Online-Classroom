package com.example.classroom;

public class responsemodellecture {
    public responsemodellecture() {
    }
    String lecturename;

    public responsemodellecture(String lecname) {
        this.lecturename = lecname;
    }

    public String getLecname() {
        return lecturename;
    }

    public void setLecname(String lecname) {
        this.lecturename = lecname;
    }
}
