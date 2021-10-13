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

import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;

public class LectureView extends AppCompatActivity {
    Button mLogOut;
    RecyclerView recView;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_lecture_view);
        checkuserexistence(); // check if alrdy logged in.
        mLogOut=findViewById(R.id.logout2);
        recView=findViewById(R.id.recyclerView2);
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
        Call<List<responsemodellecture>> call=RetrofitClient.getInstance().getApi().getLectures();
        call.enqueue(new Callback<List<responsemodellecture>>() {
            @Override
            public void onResponse(Call<List<responsemodellecture>> call, Response<List<responsemodellecture>> response) {
                List<responsemodellecture> data2=response.body();
                adapter2 ada2=new adapter2(data2, getApplicationContext());
                recView.setAdapter(ada2);
            }

            @Override
            public void onFailure(Call<List<responsemodellecture>> call, Throwable t) {
                Toast.makeText(getApplicationContext(),t.toString(),Toast.LENGTH_LONG).show();
            }
        });
    }

    public void checkuserexistence()
    {
        SharedPreferences sp=getSharedPreferences("credentials",MODE_PRIVATE);
        if(sp.contains("email")){
            Toast.makeText(LectureView.this, sp.getString("email",""), Toast.LENGTH_LONG).show();
        }
        else{
            startActivity(new Intent(getApplicationContext(), MainActivity.class));
        }
    }
}