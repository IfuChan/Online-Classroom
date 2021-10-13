package com.example.classroom;

import java.util.List;

import okhttp3.ResponseBody;
import retrofit2.Call;
import retrofit2.http.Field;
import retrofit2.http.FormUrlEncoded;
import retrofit2.http.GET;
import retrofit2.http.POST;

public interface Api {

    @FormUrlEncoded
    @POST("user-create/")
    Call<ResponseBody> createuser(
            @Field("fname") String fname,
            @Field("lname") String lname,
            @Field("email") String email,
            @Field("password") String password,
            @Field("userType") String utype,
            @Field("userimage") String usrimg
    );

    @FormUrlEncoded
    @POST("login/") //write the link of the sign in api link like the one above.
    Call<ResponseBody> verifyUser(
            @Field("email") String email,
            @Field("password") String password
    );

    @GET("course-list/")
    Call<List<responsemodel>> getCourses();

    @GET("lecture-list/")
    Call<List<responsemodellecture>> getLectures();

}