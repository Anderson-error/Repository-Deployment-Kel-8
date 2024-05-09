import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go


df =pd.read_csv("https://raw.githubusercontent.com/Anderson-error/Repository-Deployment-Kel-8/main/DATA%20CLEANED.csv")
df_file = pd.read_csv("https://raw.githubusercontent.com/Anderson-error/Repository-Deployment-Kel-8/main/Data%20Modelling.csv")

def main():
    st.set_page_config(page_title="TTEOKBEOKKI", page_icon="img/Untitled design.png", layout="wide")
    st.sidebar.image("img/Untitled design.png", use_column_width=True)
    app_mode = st.sidebar.radio("Choose your page:", ["EDA", "Model"])

    if app_mode == "EDA":
        st.markdown("<h1 style='text-align: center;'>Dashboard of Data Understanding</h1>", unsafe_allow_html=True)
    
        col1, col2, col3 = st.columns([1,1,1])
        with col1 :
            jumlah_baris = df.shape[0]  
            st.markdown(f"""
            <style>
                .box {{
                    background-color: transparent;
                    border: 1px solid #ddd;
                    border-radius: 5px;
                    padding: 10px;
                    display: flex;
                    flex-direction: column;
                    align-items: center;
                    justify-content: center;
                    height: 100%;
                }}
                .box h3 {{
                    margin-top: 0;
                    font-size: 24px;
                    color: white;
                }}
                .box p {{
                    font-size: 20px;
                    color: white;
                }}
            </style>
            <div class="box">
                <h3>Total Baris</h3>
                <p><b>{jumlah_baris}</b></p>
            </div>
            """, unsafe_allow_html=True)

        with col2 :
            total_columns = len(df.columns)
            st.markdown(f"""
                <style>
                    .box {{
                        background-color: transparent;
                        border: 1px solid #ddd;
                        border-radius: 5px;
                        padding: 10px;
                        display: flex;
                        flex-direction: column;
                        align-items: center;
                        justify-content: center;
                        height: 100%;
                    }}
                    .box h3 {{
                        margin-top: 0;
                        font-size: 24px;
                        color: white;
                    }}
                    .box p {{
                        font-size: 20px;
                        color: white;
                    }}
                </style>
                <div class="box">
                    <h3>Total Kolom</h3>
                    <p><b>{total_columns}</b></p>
                </div>
                """, unsafe_allow_html=True)
            
        with col3 :
            total_income = df['Perkiraaan Pendapatan'].sum()
            formatted_income = f"Rp. {total_income:,.0f}".replace(',', '.')
            st.markdown(f"""
                <style>
                    .box {{
                        background-color: transparent;
                        border: 1px solid #ddd;
                        border-radius: 5px;
                        padding: 10px;
                        display: flex;
                        flex-direction: column;
                        align-items: center;
                        justify-content: center;
                        height: 100%;
                    }}
                    .box h3 {{
                        margin-top: 0;
                        font-size: 24px;
                        color: white;
                    }}
                    .box p {{
                        font-size: 20px;
                        color: white;
                    }}
                </style>
                <div class="box">
                    <h3>Total Perkiraan Pendapatan</h3>
                    <p><b>{formatted_income}</b></p>
                </div>
                """, unsafe_allow_html=True)
            

        app_mode = st.selectbox("Choose your pages :", ["Distribusi", "Perbandingan", "Heat Map", "Komposisi"])

        if app_mode == "Distribusi" :
            distribusi_mode = st.selectbox("", ["Perkiraan Pendapatan", "Stok Terjual"])

            if distribusi_mode == "Perkiraan Pendapatan" :
                fig = px.bar(df, x='Nama Item', y='Perkiraaan Pendapatan',
                color='Nama Item', color_discrete_sequence=px.colors.qualitative.Set3,text='Perkiraaan Pendapatan')
                st.write('<style>div.Widget.row-widget.stRadio>div{flex-direction:row;}</style>', unsafe_allow_html=True)
                st.plotly_chart(fig, use_container_width=True)
                st.write('''
                        Bar Chart diatas merupakan hasil distribusi berdasarkan Perkiraan Pendapatan dari 6 Nama Item makanan yang berada di kedai TTEOKBEOKKI. Berdasarkan hasil diatas Nama Item makanan nomor 1 memiliki distribusi paling tinggi 
                         yang hampir menyentuh Harga Satuan 8 Miliyar.
                        ''')
                
            elif distribusi_mode == "Stok Terjual":
                fig = px.bar(df, x='Nama Item', y='Stok Terjual',
                color='Nama Item', color_discrete_sequence=px.colors.qualitative.Set3,text='Stok Terjual')
                st.write('<style>div.Widget.row-widget.stRadio>div{flex-direction:row;}</style>', unsafe_allow_html=True)
                st.plotly_chart(fig, use_container_width=True)
                st.write('''
                        Bar Chart diatas merupakan hasil distribusi berdasarkan Stok Terjual dari 6 Nama Item makanan yang berada di kedai TTEOKBEOKKI. Berdasarkan hasil diatas Nama Item makanan nomor 5 memiliki distribusi paling tinggi
                         yang menyentuh Harga Satuan lebih dari 2500 stok yang terjual.
                        ''')

        elif app_mode == "Perbandingan":
            fig = px.bar(df, x='Nama Item', y=['Total Stok', 'Stok Terjual'], barmode='group')
            st.write('<style>div.Widget.row-widget.stRadio>div{flex-direction:row;}</style>', unsafe_allow_html=True)
            st.plotly_chart(fig, use_container_width=True)
            st.write('''
                    Bar Chart diatas merupakan visualisasi perbandingan antara Total Stok dengan Stok Terjual.
                    ''')
        
        elif app_mode == "Komposisi" :
            item_counts = df['Nama Item'].value_counts()
            df_item_counts = pd.DataFrame({'Nama Item': item_counts.index, 'Frekuensi': item_counts.values})
            fig = px.pie(df_item_counts, values='Frekuensi', names='Nama Item', 
                        title='Komposisi Frekuensi Nama Item',
                        color_discrete_sequence=px.colors.qualitative.Set3)
            st.write('<style>div.Widget.row-widget.stRadio>div{flex-direction:row;}</style>', unsafe_allow_html=True)
            st.plotly_chart(fig, use_container_width=True)
            st.write('''
                    Circular Bar Chart diatas merupakan visualisasi komposisi berdasarkan Nama Item. Nama Item Makanan nomor 0 merupakan Nama Item terbanyak yaitu 17,6% dengan frekuensi sebesar 27
                    ''')

        elif app_mode == "Heat Map" :
            # st.markdown("<h3 style='text-align: center;'>Correlation Metrix</h3>", unsafe_allow_html=True)
            selected_columns = ['Total Stok','Stok Terjual','Sisa Stok']
            df_selected = df[selected_columns]
            plt.figure(figsize=(50, 6))
            fig = px.imshow(df_selected.corr(numeric_only=True))
            st.write('<style>div.Widget.row-widget.stRadio>div{flex-direction:row;}</style>', unsafe_allow_html=True)
            st.plotly_chart(fig, use_container_width=True)
            st.write('''
                    Diatas merupakan visualisasi Correlation Metrix atau Heat Map. Dari visualisasi ini menunjukkan bahwa Total Stok sangat berelasi dengan Sisa Stok dengan nilai relasi yaitu 1. 
                    ''')

        st.markdown("---")
        st.markdown("© Copyright TTEOKBEOKKI.SMD. All Rights Reserved")   

    elif app_mode == "Model":
        st.markdown("<h1 style='text-align: center;'>Dashboard of Modelling</h1>", unsafe_allow_html=True)

        model_mode = st.selectbox("Choose your pages :", ["Dataset Overview", "Clustering"])
        if model_mode == "Dataset Overview" :
            rentang_waktu = st.slider("Pilih Rentang Waktu", min_value=df['Hari'].min(), max_value=df['Hari'].max(), value=(df['Hari'].min(), df['Hari'].max()))
            data_filtered = df[(df['Hari'] >= rentang_waktu[0]) & (df['Hari'] <= rentang_waktu[1])]

            col1, col2 = st.columns([1, 1])
            with col1 :
                st.write('<style>div.Widget.row-widget.stRadio>div{flex-direction:row;}</style>', unsafe_allow_html=True)
                st.write(data_filtered, use_container_width=True)

            with col2 :
                st.write('<style>div.Widget.row-widget.stRadio>div{flex-direction:row;}</style>', unsafe_allow_html=True)
                st.write(data_filtered.describe(), use_container_width=True)
            st.write('''
                    
                    ''')
            
        elif model_mode == "Clustering":
                st.markdown("<h3 style='text-align: center;'>KMeans Cluster</h3>", unsafe_allow_html=True)

                km_mode = st.selectbox("Choose your feature :", ["Harga Satuan vs Stok Terjual", "Total Stok vs Sisa Stok", "Stok Terjual vs Perkiraan Pendapatan", "Harga Satuan vs Perkiraan Pendapatan"])
                if km_mode == "Harga Satuan vs Stok Terjual":
                    fitur_x = 'Harga Satuan'
                    fitur_y = 'Stok Terjual'
                    fig = go.Figure()
                    for cluster_id in df_file['cluster_kmeans'].unique():
                        data_cluster = df_file[df_file['cluster_kmeans'] == cluster_id]
                        fig.add_trace(go.Scatter(
                            x=data_cluster[fitur_x],
                            y=data_cluster[fitur_y],
                            mode='markers',
                            name=f'Cluster {cluster_id}',
                            marker=dict(color=cluster_id) 
                        ))
                    fig.update_layout(
                        title=f'Scatter Plot {fitur_x} vs {fitur_y}',
                        xaxis_title=fitur_x,
                        yaxis_title=fitur_y
                    )
                    st.write('<style>div.Widget.row-widget.stRadio>div{flex-direction:row;}</style>', unsafe_allow_html=True)
                    st.plotly_chart(fig, use_container_width=True)
                    st.write('''
                    Plot ini membantu melihat apakah ada pola harga dan penjualan yang berbeda antar kluster. Dengan memplot harga satuan produk di sumbu x dan jumlah stok yang terjual di sumbu y, 
                    dapat menentukan apakah ada korelasi antara harga dan jumlah barang yang terjual. 
                    ''')

                elif km_mode == "Total Stok vs Sisa Stok":
                    fitur_x = 'Total Stok'
                    fitur_y = 'Sisa Stok'
                    fig = go.Figure()
                    for cluster_id in df_file['cluster_kmeans'].unique():
                        data_cluster = df_file[df_file['cluster_kmeans'] == cluster_id]
                        fig.add_trace(go.Scatter(
                            x=data_cluster[fitur_x],
                            y=data_cluster[fitur_y],
                            mode='markers',
                            name=f'Cluster {cluster_id}',
                            marker=dict(color=cluster_id) 
                        ))
                    fig.update_layout(
                        title=f'Scatter Plot {fitur_x} vs {fitur_y}',
                        xaxis_title=fitur_x,
                        yaxis_title=fitur_y
                    )
                    st.write('<style>div.Widget.row-widget.stRadio>div{flex-direction:row;}</style>', unsafe_allow_html=True)
                    st.plotly_chart(fig, use_container_width=True)
                    st.write('''
                    Scatter plot ini memberikan wawasan tentang bagaimana stok barang dikelola di setiap kluster. Dengan memplot total stok produk di sumbu x dan sisa stok (stok yang belum terjual) di sumbu y, 
                    dapat melihat pola persediaan barang di setiap kluster.
                    Plot ini dapat membantu Anda mengidentifikasi kluster yang memiliki masalah persediaan atau yang perlu dikelola dengan lebih efisien.
                    ''')

                elif km_mode == "Stok Terjual vs Perkiraan Pendapatan":
                    fitur_x = 'Stok Terjual'
                    fitur_y = 'Perkiraaan Pendapatan'
                    fig = go.Figure()
                    for cluster_id in df_file['cluster_kmeans'].unique():
                        data_cluster = df_file[df_file['cluster_kmeans'] == cluster_id]
                        fig.add_trace(go.Scatter(
                            x=data_cluster[fitur_x],
                            y=data_cluster[fitur_y],
                            mode='markers',
                            name=f'Cluster {cluster_id}',
                            marker=dict(color=cluster_id) 
                        ))
                    fig.update_layout(
                        title=f'Scatter Plot {fitur_x} vs {fitur_y}',
                        xaxis_title=fitur_x,
                        yaxis_title=fitur_y
                    )
                    st.write('<style>div.Widget.row-widget.stRadio>div{flex-direction:row;}</style>', unsafe_allow_html=True)
                    st.plotly_chart(fig, use_container_width=True)
                    st.write('''
                    Plot ini memungkinkan untuk melihat apakah ada korelasi antara jumlah stok yang terjual dan perkiraan pendapatan di setiap kluster. Dengan memplot jumlah barang yang terjual di sumbu x dan perkiraan pendapatan di sumbu y, 
                    dapat menilai seberapa efektif suatu kluster dalam menghasilkan pendapatan dari penjualan produknya.
                    Disini dapat melihat apakah kluster dengan penjualan tinggi juga menghasilkan pendapatan yang tinggi atau sebaliknya.
                    ''')

                elif km_mode == "Harga Satuan vs Perkiraan Pendapatan":
                    fitur_x = 'Harga Satuan'
                    fitur_y = 'Perkiraaan Pendapatan'
                    fig = go.Figure()
                    for cluster_id in df_file['cluster_kmeans'].unique():
                        data_cluster = df_file[df_file['cluster_kmeans'] == cluster_id]
                        fig.add_trace(go.Scatter(
                            x=data_cluster[fitur_x],
                            y=data_cluster[fitur_y],
                            mode='markers',
                            name=f'Cluster {cluster_id}',
                            marker=dict(color=cluster_id) 
                        ))
                    fig.update_layout(
                        title=f'Scatter Plot {fitur_x} vs {fitur_y}',
                        xaxis_title=fitur_x,
                        yaxis_title=fitur_y
                    )
                    st.write('<style>div.Widget.row-widget.stRadio>div{flex-direction:row;}</style>', unsafe_allow_html=True)
                    st.plotly_chart(fig, use_container_width=True)
                    st.write('''
                    Scatter plot ini membantu untuk memahami bagaimana harga produk memengaruhi pendapatan di setiap kluster. Dengan memplot harga satuan produk di sumbu x dan perkiraan pendapatan di sumbu y, 
                    dapat melihat apakah peningkatan harga produk berdampak positif atau negatif pada pendapatan.
                    Ini dapat membantu Anda membuat keputusan strategis tentang penetapan harga produk di setiap kluster.
                    ''')
                
                selected_features = ['Nama Item','Harga Satuan','Total Stok','Stok Terjual','Sisa Stok','Perkiraaan Pendapatan']
                kmeans_mode = st.selectbox("Choose your KMeans id :", ["0","1","2"])
                if kmeans_mode == "0" :
                    cluster_id = 0
                    cluster_rows = df_file[df_file['cluster_kmeans'] == cluster_id]
                    st.write(cluster_rows[selected_features])

                elif kmeans_mode == "1" :
                    cluster_id = 1
                    cluster_rows = df_file[df_file['cluster_kmeans'] == cluster_id]
                    st.write(cluster_rows[selected_features])

                elif kmeans_mode == "2" :
                    cluster_id = 2
                    cluster_rows = df_file[df_file['cluster_kmeans'] == cluster_id]
                    st.write(cluster_rows[selected_features])

                st.write('''
                        Dalam Dataframe ini terdapat 3 KMeans Cluster id.
                        ''')
                
                kmeans_stats = df_file.groupby('cluster_kmeans').agg({
                                                                'Harga Satuan':          ['min', 'max', 'median'],
                                                                'Total Stok':            ['min', 'max', 'median'],
                                                                'Stok Terjual':          ['min', 'max', 'median'],
                                                                'Sisa Stok':             ['min', 'max', 'median'],
                                                                'Perkiraaan Pendapatan': ['min', 'max', 'median']
                                                                })
                st.write("Statistik K-Means per Fitur:")
                st.write(kmeans_stats)
                st.write('''
                        Dalam table diatas menampilkan nilai min, max dan median dari tiap-tiap kluster serta fitur. Contohnya seperti Harga Satuan nilai min 1,500,000, max 3,500,000 dan median 2,500,000.
                        ''')
                
        st.markdown("---")
        st.markdown("© Copyright TTEOKBEOKKI.SMD. All Rights Reserved")  

if __name__ == "__main__":
    st.set_option('deprecation.showfileUploaderEncoding', False)
    main()