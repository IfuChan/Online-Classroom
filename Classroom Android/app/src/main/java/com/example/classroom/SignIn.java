package com.example.classroom;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.text.TextUtils;
import android.view.View;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ProgressBar;
import android.widget.RadioButton;
import android.widget.RadioGroup;
import android.widget.Spinner;
import android.widget.TextView;
import android.widget.Toast;

import com.google.android.gms.tasks.OnCompleteListener;
import com.google.android.gms.tasks.Task;
import com.google.firebase.auth.AuthResult;
import com.google.firebase.auth.FirebaseAuth;

import org.jetbrains.annotations.NotNull;

import java.io.IOException;

import okhttp3.ResponseBody;
import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;

public class SignIn extends AppCompatActivity {
    EditText mEmail,mPassword;
    Button mLoginBtn;
    TextView mRegBtn;
    ProgressBar progressBar;
    RadioGroup radgrp;
    RadioButton radbtn;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_sign_in);

        mEmail=findViewById(R.id.semail);
        mPassword=findViewById(R.id.spassword);
        progressBar=findViewById(R.id.progressBar2);
        mLoginBtn=findViewById(R.id.signinButton);
        mRegBtn=findViewById(R.id.signReg);
        radgrp=findViewById(R.id.radioGroup3);
        checkuserexistence();
        mLoginBtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                String email=mEmail.getText().toString().trim();
                String password= mPassword.getText().toString().trim();

                if(TextUtils.isEmpty(email)){       //checking whether it is empty or not
                    mEmail.setError("Email is required");
                    return;
                }

                if(TextUtils.isEmpty(password)){
                    mEmail.setError("Password is required");
                    return;
                }

                Call<ResponseBody> call=RetrofitClient.getInstance().getApi().verifyUser(email,password);
                call.enqueue(new Callback<ResponseBody>() {
                    @Override
                    public void onResponse(Call<ResponseBody> call, Response<ResponseBody> response) {
                        /*String sy= null;
                        try {
                            sy = response.body().string();
                        } catch (IOException e) {
                            e.printStackTrace();
                        }
                        //Toast.makeText(SignIn.this, sy, Toast.LENGTH_LONG).show();
                        String test1="\"exist\"";
                        if(sy.equals(test1)){

                            startActivity(new Intent(getApplicationContext(), LoggedInHpage.class));
                        }
                        else{
                            Toast.makeText(SignIn.this, "Invalid Email or Password", Toast.LENGTH_LONG).show();
                        }*/
                        String sy= null;
                        try {
                            sy = response.body().string();
                        } catch (IOException e) {
                            e.printStackTrace();
                        }
                        String test1="\"exist\"";
                        if(sy.equals(test1))
                        {
                                //Toast.makeText(SignIn.this, "I am here x1", Toast.LENGTH_LONG).show();
                                SharedPreferences sp=getSharedPreferences("credentials",MODE_PRIVATE);
                                SharedPreferences.Editor editor=sp.edit();
                                editor.putString("email", mEmail.getText().toString());
                                editor.putString("password", mPassword.getText().toString());
                                editor.commit();
                                editor.apply();
                                Toast.makeText(SignIn.this, "Sign In Successful!", Toast.LENGTH_LONG).show();
                                int radioId=radgrp.getCheckedRadioButtonId();
                                radbtn=findViewById(radioId);
                                if(radbtn.getText().toString().trim().equals("Student")){
                                    startActivity(new Intent(getApplicationContext(), LoggedInHpage.class));
                                    finish();
                                }
                                else if(radbtn.getText().toString().trim().equals("Teacher")){
                                    startActivity(new Intent(getApplicationContext(), LogInTHpage.class));
                                    finish();
                                }

                        }
                        else
                        {
                            Toast.makeText(SignIn.this, "Invalid Email or Password", Toast.LENGTH_LONG).show();
                        }
                    }

                    @Override
                    public void onFailure(Call<ResponseBody> call, Throwable t) {
                        Toast.makeText(SignIn.this, t.getMessage(), Toast.LENGTH_LONG).show();
                    }
                });

                progressBar.setVisibility(View.VISIBLE);

            }
        });
        mRegBtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                startActivity(new Intent(getApplicationContext(),Reg.class));
            }
        });
    }
    void processLogin(String email, String password)
    {
        //Call<ResponseBody> call=RetrofitClient.getInstance().getApi().createuser(fname,lname,email,password,utype,usrimg);
        Call<ResponseBody> call=RetrofitClient.getInstance().getApi().verifyUser(email,password);
        call.enqueue(new Callback<ResponseBody>() {
            @Override
            public void onResponse(Call<ResponseBody> call, Response<ResponseBody> response) {
                String sy = null;
                try {
                    sy = response.body().string();
                } catch (IOException e) {
                    e.printStackTrace();
                }
                Toast.makeText(SignIn.this, sy, Toast.LENGTH_LONG).show();
                if(sy.equals("failed")) {
                    Toast.makeText(SignIn.this, "Invalid Email or Password", Toast.LENGTH_LONG).show();
                }
                else if(sy.equals("exist")) {
                    Toast.makeText(SignIn.this, "I am here x1", Toast.LENGTH_LONG).show();
                    SharedPreferences sp = getSharedPreferences("credentials", MODE_PRIVATE);
                    SharedPreferences.Editor editor = sp.edit();
                    editor.putString("email", mEmail.getText().toString());
                    editor.putString("password", mPassword.getText().toString());
                    editor.commit();
                    editor.apply();
                    Toast.makeText(SignIn.this, "Sign In Successful!", Toast.LENGTH_LONG).show();
                    startActivity(new Intent(getApplicationContext(), LoggedInHpage.class));
                    finish();
                }
            }

            @Override
            public void onFailure(Call<ResponseBody> call, Throwable t) {
                Toast.makeText(SignIn.this, t.getMessage(), Toast.LENGTH_LONG).show();
            }
        });
    }

    void checkuserexistence()
    {
        SharedPreferences sp=getSharedPreferences("credentials",MODE_PRIVATE);
        if(sp.contains("email"))
        {
            startActivity(new Intent(getApplicationContext(),LoggedInHpage.class));
        }
        else {
            //Toast.makeText(SignIn.this, "Please login", Toast.LENGTH_LONG).show();
        }
    }
}