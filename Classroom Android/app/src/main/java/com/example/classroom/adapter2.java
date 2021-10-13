package com.example.classroom;

import android.content.Context;
import android.content.Intent;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

import org.jetbrains.annotations.NotNull;

import java.util.List;

public class adapter2 extends RecyclerView.Adapter<adapter2.ViewHolder>  {
        List<responsemodellecture> data;
        Context context;
    public adapter2 (List<responsemodellecture> data, Context context) {
        this.data = data;
        this.context=context;
    }

    @NonNull
    @NotNull
    @Override
    public adapter2.ViewHolder onCreateViewHolder(@NonNull @NotNull ViewGroup parent, int viewType) {
        View view= LayoutInflater.from(parent.getContext()).inflate(R.layout.lecitems,parent,false);
        return new adapter2.ViewHolder(view);
    }

    @Override
    public void onBindViewHolder(@NonNull @NotNull adapter2.ViewHolder holder, int position) {
        holder.Lecname.setText(data.get(position).getLecname());
        holder.Lecname.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent=new Intent(context,pdfViewer.class);
                intent.setFlags(Intent.FLAG_ACTIVITY_NEW_TASK);
                context.startActivity(intent);
            }
        });
    }

    @Override
    public int getItemCount() {
        return data.size();
    }

    class ViewHolder extends RecyclerView.ViewHolder{
        TextView Lecname;

        public ViewHolder(@NonNull View itemView) {
            super(itemView);
            Lecname=itemView.findViewById(R.id.lecturename);
        }
    }
}
