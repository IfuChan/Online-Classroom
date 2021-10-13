package com.example.classroom;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.text.TextUtils;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ProgressBar;
import android.widget.RadioButton;
import android.widget.RadioGroup;
import android.widget.TextView;
import android.widget.Toast;


import java.io.IOException;

import okhttp3.ResponseBody;
import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;

public class Reg extends AppCompatActivity {

    EditText mFirstName,mLastName , mEmail, mPassword, mrePassword;
    Button mRegBtn;
    TextView mLoginBtn;
    ProgressBar progressbar;
    RadioGroup radgrp;
    RadioButton radbtn;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_reg);

        mFirstName=findViewById(R.id.fname);
        mLastName=findViewById(R.id.lname);
        mEmail=findViewById(R.id.email);
        mPassword=findViewById(R.id.password);
        mrePassword=findViewById(R.id.rePassword);
        mRegBtn=findViewById(R.id.regButton);
        mLoginBtn=findViewById(R.id.regLogin);
        radgrp=findViewById(R.id.radioGroup2);

        progressbar=findViewById(R.id.progressBar);



        mRegBtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                String fname=mFirstName.getText().toString().trim();
                String lname=mLastName.getText().toString().trim();
                String email=mEmail.getText().toString().trim();
                String password= mPassword.getText().toString().trim();
                int radioId=radgrp.getCheckedRadioButtonId();
                radbtn=findViewById(radioId);
                String utype= (String) radbtn.getText();
                String usrimg=null;
                String rePassword=mrePassword.getText().toString().trim();

                if(TextUtils.isEmpty(email)){       //checking whether it is empty or not
                    mEmail.setError("Email is required");
                    return;
                }

                if(TextUtils.isEmpty(password)){
                    mEmail.setError("Password is required");
                    return;
                }

                if(!password.equals(rePassword)){
                    mrePassword.setError("Passwords do not match");
                    return;
                }

                if(password.length() <6)
                {
                    mPassword.setError("Password must be minimum six characters long");
                }

                progressbar.setVisibility(View.VISIBLE);

                //As all requirements are fulfilled, start registering user .
                Call<ResponseBody> call=RetrofitClient.getInstance().getApi().createuser(fname,lname,email,password,utype,usrimg);
                call.enqueue(new Callback<ResponseBody>() {
                    @Override
                    public void onResponse(Call<ResponseBody> call, Response<ResponseBody> response) {
                        try {
                            String sy= response.body().string();
                            Toast.makeText(Reg.this, sy, Toast.LENGTH_LONG).show();
                        } catch (IOException e) {
                            e.printStackTrace();
                        }
                    }

                    @Override
                    public void onFailure(Call<ResponseBody> call, Throwable t) {
                        Toast.makeText(Reg.this, t.getMessage(), Toast.LENGTH_LONG).show();
                    }
                });
                startActivity(new Intent(getApplicationContext(),SignIn.class));
            }
        });
        mLoginBtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                startActivity(new Intent(getApplicationContext(),SignIn.class));
            }
        });
    }
}