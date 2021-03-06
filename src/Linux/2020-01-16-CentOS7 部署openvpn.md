---
layout: post
title: CentOS7部署openvpn
slug: openvpn-in-centos7
date: 2020-01-16 12:00
status: publish
author: Dragon
categories: 
  - Linux
tags: 
  - Linux
  - Openvpn
excerpt: 暂无加入用户认证
---

### 安装软件包
```
yum install -y epel-release
yum install -y openvpn easy-rsa openssl openssl-devel lzo lzo-devel pam pam-devel automake pkgconfig
```

### server端 制作证书，密钥等文件
```
# 复制服务端配置文件至openvpn的根目录
cp /usr/share/doc/openvpn-2.4.8/sample/sample-config-files/server.conf /etc/openvpn/

# 创建制作证书目录
mkdir /etc/openvpn/easy-rsa

cd /etc/openvpn/

# 复制制作证书工具至制作证书目录
cp -r /usr/share/easy-rsa/3.0.6/* /etc/openvpn/easy-rsa/

cd easy-rsa/

# 创建证书配置信息
vim vars
set_var EASYRSA_REQ_COUNTRY     "CN"        # 国家
set_var EASYRSA_REQ_PROVINCE    "HB"        # 省份
set_var EASYRSA_REQ_CITY        "Wuhan"     # 城市
set_var EASYRSA_REQ_ORG         "dragon"    # 组织
set_var EASYRSA_REQ_EMAIL       "xx@xx.com" # 邮箱
set_var EASYRSA_REQ_OU          "dragon"    # 拥有者

# 初始化pki，生成目录文件结构
./easyrsa init-pki
init-pki complete; you may now create a CA or requests.
your newly created PKI dir is: /etc/openvpn/easy-rsa/pki

# 使用vars文件里面配置的信息创建ca证书,中间会提示输入密码,记住此密码,后期需要使用
./easyrsa build-ca
Note: using Easy-RSA configuration from: ./vars # 使用vars文件里面配置的信息
Generating a 2048 bit RSA private key

writing new private key to '/etc/openvpn/easy-rsa/pki/private/ca.key.Lg8IKADc4Q'
Enter PEM pass phrase:# 设置ca密码
Verifying - Enter PEM pass phrase:# 重新输入上面的密码
-----
You are about to be asked to enter information that will be incorporated
into your certificate request.
What you are about to enter is what is called a Distinguished Name or a DN.
There are quite a few fields but you can leave some blank
For some fields there will be a default value,
If you enter '.', the field will be left blank.
-----
Common Name (eg: your user, host, or server name) [Easy-RSA CA]:# 直接回车,就是默认的CA作为名字,也可自定义,本次使用opserver
CA creation complete and you may now import and sign cert requests.
Your new CA certificate file for publishing is at:
/etc/openvpn/easy-rsa/pki/ca.crt

# nopass设置免证书密码，如果要设置密码可以取消此参数选项,设置CommonName的时候可使用默认的server,也可自定义.
./easyrsa gen-req opserver nopass
Note: using Easy-RSA configuration from: ./vars                             #使用vars文件里面配置的信息
Generating a 2048 bit RSA private key

writing new private key to '/etc/openvpn/easy-rsa/pki/private/opserver.key.yuG9HRsSlU'
-----
You are about to be asked to enter information that will be incorporated
into your certificate request.
What you are about to enter is what is called a Distinguished Name or a DN.
There are quite a few fields but you can leave some blank
For some fields there will be a default value,
If you enter '.', the field will be left blank.
-----
Common Name (eg: your user, host, or server name) [server]:# 直接回车,默认名字为server,也可自定义,本次使用opserver
Keypair and certificate request completed. Your files are:
req: /etc/openvpn/easy-rsa/pki/reqs/opserver.req
key: /etc/openvpn/easy-rsa/pki/private/opserver.key

# 第二个server是只上面服务端证书的CommonName名字，本次使用opserver
./easyrsa sign server opserver
You are about to sign the following certificate.
Please check over the details shown below for accuracy. Note that this request
has not been cryptographically verified. Please be sure it came from a trusted
source or that you have verified the request checksum with the sender.
 
Request subject, to be signed as a server certificate for 3650 days:
 
subject=
    commonName                = opserver
 
Type the word 'yes' to continue, or any other input to abort.
  Confirm request details: yes
Using configuration from ./openssl-1.0.cnf
Enter pass phrase for /etc/openvpn/easy-rsa/pki/private/ca.key:            #输入上面ca证书生成时的密码
Check that the request matches the signature
Signature ok
The Subject's Distinguished Name is as follows
commonName            :PRINTABLE:'opserver'
Certificate is to be certified until Jan 14 09:11:12 2029 GMT (3650 days)
Write out database with 1 new entries
Data Base Updated
Certificate created at: /etc/openvpn/easy-rsa/pki/issued/opserver.crt          #服务端证书路径

# 创建Diffie-Hellman，时间有点长
./easyrsa gen-dh
Note: using Easy-RSA configuration from: ./vars
Generating DH parameters, 2048 bit long safe prime, generator 2
This is going to take a long time

DH parameters of size 2048 created at /etc/openvpn/pki/dh.pem                 #dh证书路径

cd /etc/openvpn

# 生成ta.key
openvpn --genkey --secret ta.key
```

### 客户端证书
```
# 为了便于区别，我们把客户端使用的证书存放在新的路径。/etc/openvpn/client,证书制作流程如server
mkdir -p /etc/openvpn/client

cd /etc/openvpn/client

cp -r /usr/share/easy-rsa/3.0.6/* /etc/openvpn/client

cp /usr/share/doc/easy-rsa-3.0.6/vars.example ./vars

./easyrsa init-pki

./easyrsa gen-req opclient nopass

cd /etc/openvpn/easy-rsa

./easyrsa import-req /etc/openvpn/client/pki/reqs/opclient.req opclient

./easyrsa sign client opclient

# 将制作好的server证书放在openvpn的根目录,方便配置文件读取
cp /etc/openvpn/easy-rsa/pki/ca.crt /etc/openvpn/
cp /etc/openvpn/easy-rsa/pki/private/opserver.key /etc/openvpn/
cp /etc/openvpn/easy-rsa/pki/issued/opserver.crt /etc/openvpn/
cp /etc/openvpn/easy-rsa/pki/dh.pem /etc/openvpn/

cd /etc/openvpn/

# server配置文件
vim server.conf
cat /etc/openvpn/server.conf
local 0.0.0.0
port 1194
proto tcp
dev tun
ca ca.crt
cert opserver.crt
key opserver.key
dh dh.pem
server 10.8.0.0 255.255.255.0
ifconfig-pool-persist ipp.txt
push "redirect-gateway def1 bypass-dhcp"
push "dhcp-option DNS 8.8.8.8"
push "dhcp-option DNS 114.114.114.114"
keepalive 10 120
tls-auth ta.key 0
cipher AES-256-CBC
comp-lzo
persist-key
persist-tun
status openvpn-status.log
verb 3

# 启动openvpn-server并开机启动
systemctl -f enable openvpn@server.service
systemctl start openvpn@server.service

# 下载客户端证书至本地
sz /etc/openvpn/easy-rsa/pki/issued/client.crt
sz /etc/openvpn/client/pki/private/client.key
sz /etc/openvpn/easy-rsa/pki/ca.crt
sz /etc/openvpn/ta.key
```

### 开启OpenVPN服务器的网卡转发功能
```
echo "net.ipv4.ip_forward = 1" ######/etc/sysctl.conf
sysctl -p
```
  
### 添加nat规则并生效
```
iptables -t nat -A POSTROUTING -s 10.8.0.0/24 -o enp0s31f6 -j MASQUERADE
iptables-save
```

### 客户端配置文件client.opvn
```
client
dev tun   
proto tcp
remote server端IP 1194
resolv-retry infinite
nobind
persist-key
persist-tun
remote-cert-tls server
ca ca.crt
cert opclient.crt
key opclient.key
tls-auth ta.key 1
cipher AES-256-CBC
comp-lzo
verb 3  
```

### 将下载到本地的客户端证书和客户端配置文件拷贝至openvpn目录的config目录中

### 启动

### 参考: [Centos7 安装openvpn by easy-rsa3.0](https://segmentfault.com/a/1190000019502850) 操作整理