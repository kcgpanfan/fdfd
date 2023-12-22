import streamlit as st

def main():
    st.set_page_config(
        page_title="即時案件",
        page_icon=":clipboard:",
        layout="wide"
    )
    
    st.markdown(
        """
        <style>
        body {
            background-image: url("http://127.0.0.1:8080/bg.png");
            background-repeat: no-repeat;
            background-size: cover;
        }
        #caseListTable td, #caseListTable th {
            font-size: 23px; 
        }
        #caseListTable {
            transform: rotate(180deg);
            -ms-transform: rotate(180deg);
            -webkit-transform: rotate(180deg);
            direction: rtl;
        }
        #caseListTable td, #caseListTable th {
            transform: rotate(-180deg);
            -ms-transform: rotate(-180deg);
            -webkit-transform: rotate(-180deg);
            direction: ltr;
        }
        .tablelist {
            border-collapse: collapse;
            padding-left: 2px;
            padding-right: 2px;
            padding-top: 1px;
        }
        .tablelist th {
            border-right: 1px solid #6CBF95;
            border-left: 1px solid #6CBF95;
            font-weight: bold;
            background-color: #48B28E;
            padding: 4px;
            color: #FFFFFF;
        }
        .table_tr1 {
            background-color: #F6E6C8;
        }
        .tablelist td {
            border-top: 1px solid #D9D9D9;
            border-right: 1px solid #6BC1A4;
            border-left: 1px solid #6BC1A4;
            padding: 4px;
        }
        .map_btn {
            color: #004eb9;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    
    st.markdown(
        """
        <table id="caseListTable" width="100%" height="200px" class="tablelist" style="border:2px #6ABDA1 solid">
        {% for row in data.csno %}
            <tr class="table_tr1 rainbow">
                <td align="center">{{ data.dept[loop.index0] }}</td>
                <td align="center">{{ data.in_time[loop.index0] }}</td>
                <td align="center">{{ data.nt_tel[loop.index0] }}</td>
                <td align="center">{{ data.dis_code[loop.index0] }}</td>
                <td align="center">
                    <a href="https://www.google.com.tw/maps/search/{{ data.cs_place[loop.index0] }}" onclick="openModal('{{ data.cs_place[loop.index0] }}'); return false;">{{ data.cs_place[loop.index0] }}</a>
                </td>
                <td align="center">{{ data.nt_name[loop.index0] }}</td>
                <td align="center">{{ data.memo[loop.index0] }}</td>
            </tr>
        {% endfor %}
        </table>
        <script type="text/javascript">
        (function () {
            var script = document.createElement('script');
            script.src = "https://cdn.jsdelivr.net/npm/eruda";
            document.body.append(script);
            script.onload = function () {
                eruda.init();
            }
        })();
        </script>
        """,
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()