package com.example.classroom;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.Toast;

public class LogInTHpage extends AppCompatActivity {
    Button mLogOut;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_log_in_thpage);
        mLogOut=findViewById(R.id.logoutT);
        checkuserexistence(); // check if alrdy logged in.

        mLogOut.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                SharedPreferences sp=getSharedPreferences("credentials",MODE_PRIVATE);
                sp.edit().remove("email").commit();
                sp.edit().remove("password").commit();
                sp.edit().apply();
                startActivity(new Intent(getApplicationContext(),MainActivity.class));
                finish();
            }
        });
    }

    public void checkuserexistence()
    {
        SharedPreferences sp=getSharedPreferences("credentials",MODE_PRIVATE);
        if(sp.contains("email")){
            Toast.makeText(LogInTHpage.this, sp.getString("email",""), Toast.LENGTH_LONG).show();
        }
        else{
            startActivity(new Intent(getApplicationContext(), MainActivity.class));
        }
    }
}