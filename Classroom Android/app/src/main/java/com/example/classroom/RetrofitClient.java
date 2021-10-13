package com.example.classroom;

import retrofit2.Retrofit;
import retrofit2.converter.gson.GsonConverterFactory;
///http://api/" 10.0.2.2  10.0.2.16  192.168.0.107 127.0.0.1

public class RetrofitClient {
    private static final String Base_Url ="http://192.168.0.107:8001/api/";
    private static RetrofitClient mInstance;
    private Retrofit retrofit;

    private RetrofitClient(){
        retrofit=new Retrofit.Builder()
                .baseUrl(Base_Url)
                .addConverterFactory(GsonConverterFactory.create())
                .build();
    }

    public static synchronized RetrofitClient getInstance(){
        if(mInstance==null){
            mInstance=new RetrofitClient();
        }
        return mInstance;
    }

    public Api getApi(){
        return retrofit.create(Api.class);
    }
}
