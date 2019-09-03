#!/usr/bin/env python3

import sys
import pandas as pd
import plotly.express as px

def main():
    if len(sys.argv) > 1:
        try:
            df = pd.read_csv(sys.argv[1])
            y_array=list(df['y'].to_numpy())
            max_y=max(y_array)
            avg_y=sum(y_array)/len(y_array)
            min_y=min(y_array)
            plot_title=f'Min: {min_y} Avg: {avg_y} Max: {max_y}'
            if (len(sys.argv) > 2) and (sys.argv[2] == "--bar"):
                fig = px.bar(df, x='x', y='y', title=plot_title)
            else:
                fig = px.line(df, x='x', y='y', title=plot_title)
            fig.show()
        except Exception as e:
            print(f"error: {str(e)}")
    else:
        print(f"Usage: {sys.argv[0]} <data_path.csv> [OPTIONS]\nOptions:\n\t--line - Shows line chart (default)\n\t      OR\n\t--bar  - Shows bar chart\n\nData format: x,y\\n<[x value,y value\\n]*\nExample:\n\tx,y\n\t1,2\n\t3,4\n\t5,6\n ")
main()
