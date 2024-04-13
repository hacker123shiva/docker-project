package com.server.myserver.entities;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@AllArgsConstructor
@NoArgsConstructor
public class Sentiment {
    public double polarity;
    public String sentiment;
    public double subjectivity;
}