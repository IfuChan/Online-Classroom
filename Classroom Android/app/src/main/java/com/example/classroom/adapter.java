package com.example.classroom;

import android.content.Context;
import android.content.Intent;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ImageView;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

import org.jetbrains.annotations.NotNull;

import java.util.List;

public class adapter extends RecyclerView.Adapter<adapter.ViewHolder> {

    public adapter(List<responsemodel> data, Context context) {
        this.data = data;
        this.context=context;
    }
    List<responsemodel> data;
    Context context;

    @NonNull
    @NotNull
    @Override
    public ViewHolder onCreateViewHolder(@NonNull @NotNull ViewGroup parent, int viewType) {
        View view= LayoutInflater.from(parent.getContext()).inflate(R.layout.items,parent,false);
        return new ViewHolder(view);
    }

    @Override
    public void onBindViewHolder(@NonNull @NotNull adapter.ViewHolder holder, int position) {
        holder.title.setText(data.get(position).getCoursename());
        holder.sem.setText(data.get(position).getSemester());
        holder.desc.setText(data.get(position).getDesc());
        holder.title.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent=new Intent(context,LectureView.class);
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
        TextView title,sem,desc;

        public ViewHolder(@NonNull View itemView) {
            super(itemView);
            title=itemView.findViewById(R.id.Title);
            sem=itemView.findViewById(R.id.sem);
            desc=itemView.findViewById(R.id.desc);
        }
    }
}
