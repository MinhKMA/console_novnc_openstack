
- Cài đặt python3.5

```sh
yum -y install https://centos7.iuscommunity.org/ius-release.rpm
yum -y install python35u
yum -y install python35u-pip
yum install python35u-devel -y
```

- Cài đặt python-openstackclient

```pip3 install python-openstackclient```

- Clone source code 

```git clone git@github.com:MinhKMA/console_novnc_openstack.git```

- Chỉnh sửa biến môi trường để xác thực với openstack trong `conf.py`

- Hiển thị url console của tất cả các VM

```python3 get_url.py```

output:

```sh 
vm01 : {'console': {'type': 'novnc', 'url': 'http://192.168.100.75:6080/vnc_auto.html?token=58a7f011-5133-4ae0-8163-260b2a88b673'}}
minhmumit : {'console': {'type': 'novnc', 'url': 'http://192.168.100.75:6080/vnc_auto.html?token=501eb4b6-7d67-4fd7-ab5f-7a93b3274c7e'}}
```

- Copy url và sử dụng trình duyệt của bạn paste url thu được và thưởng thức :)  

