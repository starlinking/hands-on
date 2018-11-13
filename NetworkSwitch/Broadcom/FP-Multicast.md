<details>
  <summary>Configure the switch for static forwarding of multicast addressed flows
  </summary>
<p>

#### Statically configure multicast forwarding table with IGMP Snooping turned off

```shell
(Switching) #config

(Switching)  (Config)#class-map match-all mip ipv4

(Switching)  (Config-classmap)#match dstip 224.0.0.0 255.0.0.0

(Switching)  (Config-classmap)#exit

(Switching)  (Config)#policy-map VIDEO1_4K_POLICY in

(Switching)  (Config-policy-map)#class mip

(Switching)  (Config-policy-classmap)#redirect 1/0/13

(Switching)  (Config-policy-classmap)#exit

(Switching)  (Config-policy-map)#exit

(Switching)  (Config)#interface 1/0/2

(Switching)  (Interface 1/0/2)#service-policy in VIDEO1_4K_POLICY

(Switching)  (Interface 1/0/2)#exit

(Switching)  (Config)#exit

(Switching)  #show policy-map interface 1/0/2 in
```
</p>
</details>
