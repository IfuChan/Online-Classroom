package com.example.classroom;

public class responsemodel {
    String id, coursename, semester, desc;

    public responsemodel() {
    }

    public responsemodel(String id, String coursename, String semester, String desc) {
        this.id = id;
        this.coursename = coursename;
        this.semester = semester;
        this.desc = desc;
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public String getCoursename() {
        return coursename;
    }

    public void setCoursename(String coursename) {
        this.coursename = coursename;
    }

    public String getSemester() {
        return semester;
    }

    public void setSemester(String semester) {
        this.semester = semester;
    }

    public String getDesc() {
        return desc;
    }

    public void setDesc(String desc) {
        this.desc = desc;
    }
}
