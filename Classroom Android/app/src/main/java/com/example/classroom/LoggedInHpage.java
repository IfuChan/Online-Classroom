package com.example.classroom;

import androidx.appcompat.app.AppCompatActivity;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.Toast;

import java.util.List;

import okhttp3.ResponseBody;
import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;


public class LoggedInHpage extends AppCompatActivity {
    Button mLogOut;
    RecyclerView recView;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_logged_in_hpage);
        mLogOut=findViewById(R.id.logout);
        checkuserexistence(); // check if alrdy logged in.
        recView=findViewById(R.id.recyclerView);

        recView.setLayoutManager(new LinearLayoutManager(this));

        processData();


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

    public void processData(){
        //Call<ResponseBody> call=RetrofitClient.getInstance().getApi().createuser(fname,lname,email,password,utype,usrimg);
        Call<List<responsemodel>> call=RetrofitClient.getInstance().getApi().getCourses();
        call.enqueue(new Callback<List<responsemodel>>() {
            @Override
            public void onResponse(Call<List<responsemodel>> call, Response<List<responsemodel>> response) {
                List<responsemodel> data=response.body();
                adapter ada=new adapter(data, getApplicationContext());
                recView.setAdapter(ada);
            }

            @Override
            public void onFailure(Call<List<responsemodel>> call, Throwable t) {
                Toast.makeText(getApplicationContext(),t.toString(),Toast.LENGTH_LONG).show();
            }
        });
    }

    public void checkuserexistence()
    {
        SharedPreferences sp=getSharedPreferences("credentials",MODE_PRIVATE);
        if(sp.contains("email")){
            Toast.makeText(LoggedInHpage.this, sp.getString("email",""), Toast.LENGTH_LONG).show();
        }
        else{
        startActivity(new Intent(getApplicationContext(), MainActivity.class));
        }
    }
}