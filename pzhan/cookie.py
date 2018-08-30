b = 'first_visit_datetime_pc=2018-08-24+15%3A45%3A00; p_ab_id=4; p_ab_id_2=5; yuid=FxlliJc76; __utma=235335808.1873689210.1535093030.1535093030.1535093030.1; __utmc=235335808; __utmz=235335808.1535093030.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmt=1; tag_view_ranking=y8GNntYHsi~BU9SQkS-zU~ueeKYaEKwj~144zWY--zX~fafuO7KcEk~jl9Gy4v1Ny~ya2M5yc9BW~xZ6jtQjaj9; _ga=GA1.2.661695032.1534239892; _gid=GA1.2.324695742.1535093057; _gat=1; login_bc=1; PHPSESSID=14704921_447e241ea4dd76dbf944f2e6cd8fe770; device_token=37c73b90c5b7e513abff3af8c0e8aef1; privacy_policy_agreement=1; c_type=23; a_type=0; b_type=1; __utmv=235335808.|2=login%20ever=no=1^3=plan=normal=1^5=gender=male=1^6=user_id=14704921=1^9=p_ab_id=4=1^10=p_ab_id_2=5=1^11=lang=zh=1; __utmb=235335808.3.9.1535093033947'
cookie ={}
for line in b.split(';'):
    
    key,value = line.split('=',1)
    cookie[key] = value
print(cookie)