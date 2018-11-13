# hands-on
All Best Practices about Networking, Automation, Virtualization, Cloud and DevOps

## FASTPATH::Multicast

<details>
  <summary>Configure the switch for static forwarding of multicast addressed flows
  </summary>
<p>

#### Statically configure multicast forwarding table with IGMP Snooping turned off

```shell
(DataPlane Switching) #config

(DataPlane Switching)  (Config)#class-map match-all mip ipv4

(DataPlane Switching)  (Config-classmap)#match dstip 224.0.0.0 255.0.0.0

(DataPlane Switching)  (Config-classmap)#exit

(DataPlane Switching)  (Config)#policy-map VIDEO1_4K_POLICY in

(DataPlane Switching)  (Config-policy-map)#class mip

(DataPlane Switching)  (Config-policy-classmap)#redirect 1/0/13

(DataPlane Switching)  (Config-policy-classmap)#exit

(DataPlane Switching)  (Config-policy-map)#exit

(DataPlane Switching)  (Config)#interface 1/0/2

(DataPlane Switching)  (Interface 1/0/2)#service-policy in VIDEO1_4K_POLICY

(DataPlane Switching)  (Interface 1/0/2)#exit

(DataPlane Switching)  (Config)#exit

(DataPlane Switching)  #show policy-map interface 1/0/2 in
```
</p>
</details>
