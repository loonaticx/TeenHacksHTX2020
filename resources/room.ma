//Maya ASCII 2019 scene
//Name: room.ma
//Last modified: Sat, May 30, 2020 04:18:59 AM
//Codeset: 1252
requires maya "2019";
requires "mtoa" "3.1.2";
currentUnit -l centimeter -a degree -t film;
fileInfo "application" "maya";
fileInfo "product" "Maya 2019";
fileInfo "version" "2019";
fileInfo "cutIdentifier" "201812112215-434d8d9c04";
fileInfo "osv" "Microsoft Windows 10 Technical Preview  (Build 18362)\n";
fileInfo "license" "student";
createNode transform -s -n "persp";
	rename -uid "263E7A7D-4314-4402-61F6-23A613873BF7";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 78.571122291626978 2.6418767509978807 26.460549435713848 ;
	setAttr ".r" -type "double3" 0.86164727038978883 80.599999999999753 0 ;
createNode camera -s -n "perspShape" -p "persp";
	rename -uid "1B57D280-4157-3245-7A16-4EB84DE66086";
	setAttr -k off ".v" no;
	setAttr ".fl" 34.999999999999993;
	setAttr ".coi" 84.151390305242884;
	setAttr ".imn" -type "string" "persp";
	setAttr ".den" -type "string" "persp_depth";
	setAttr ".man" -type "string" "persp_mask";
	setAttr ".hc" -type "string" "viewSet -p %camera";
	setAttr ".ai_translator" -type "string" "perspective";
createNode transform -s -n "top";
	rename -uid "A1509993-46D1-D730-9C31-F19B976AB67D";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 0 1000.1 0 ;
	setAttr ".r" -type "double3" -90 0 0 ;
createNode camera -s -n "topShape" -p "top";
	rename -uid "228D1CA6-4286-680D-C6F4-0EAF1F29B1E4";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 1000.1;
	setAttr ".ow" 30;
	setAttr ".imn" -type "string" "top";
	setAttr ".den" -type "string" "top_depth";
	setAttr ".man" -type "string" "top_mask";
	setAttr ".hc" -type "string" "viewSet -t %camera";
	setAttr ".o" yes;
	setAttr ".ai_translator" -type "string" "orthographic";
createNode transform -s -n "front";
	rename -uid "74779C4C-4650-C845-C90A-FBBD1E1D02A9";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 0 0 1000.1 ;
createNode camera -s -n "frontShape" -p "front";
	rename -uid "D277EBB6-4977-DC94-4C12-55AB8C42D04C";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 1000.1;
	setAttr ".ow" 30;
	setAttr ".imn" -type "string" "front";
	setAttr ".den" -type "string" "front_depth";
	setAttr ".man" -type "string" "front_mask";
	setAttr ".hc" -type "string" "viewSet -f %camera";
	setAttr ".o" yes;
	setAttr ".ai_translator" -type "string" "orthographic";
createNode transform -s -n "side";
	rename -uid "9A12C611-42DD-67E4-6ADB-2284E39536DB";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 1000.1 0 0 ;
	setAttr ".r" -type "double3" 0 90 0 ;
createNode camera -s -n "sideShape" -p "side";
	rename -uid "FCA3B8B8-4A12-B729-9166-D2ACCAE55674";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 1000.1;
	setAttr ".ow" 30;
	setAttr ".imn" -type "string" "side";
	setAttr ".den" -type "string" "side_depth";
	setAttr ".man" -type "string" "side_mask";
	setAttr ".hc" -type "string" "viewSet -s %camera";
	setAttr ".o" yes;
	setAttr ".ai_translator" -type "string" "orthographic";
createNode transform -n "ROOM";
	rename -uid "24F19699-4F33-5549-CB3C-B58FCC2EC6BA";
createNode transform -n "pasted__room1" -p "ROOM";
	rename -uid "165DBD6E-4B08-2B60-4759-2289860E170F";
	setAttr ".t" -type "double3" -9.3087768260412087 33.182529425846582 18.157618175628244 ;
	setAttr ".r" -type "double3" 0 270 180 ;
	setAttr ".s" -type "double3" 1.6620864049942878 1.2463779114912545 1.5430197509225698 ;
	setAttr ".rp" -type "double3" 0.91805295755752014 -9.4356098741389935 -7.7832937129483115 ;
	setAttr ".sp" -type "double3" -0.37452560925093292 0.55492509528688461 -2.9021995422162101 ;
	setAttr ".spt" -type "double3" 1.2925785668084389 -9.9905349694259318 -4.8810941707320907 ;
createNode mesh -n "pasted__room1Shape" -p "pasted__room1";
	rename -uid "919C85D1-4D98-C051-C5FF-2A8654DC94CE";
	setAttr -k off ".v";
	setAttr -s 3 ".iog[0].og";
	setAttr ".iog[0].og[0].gcl" -type "componentList" 4 "f[0:2]" "f[4:8]" "f[10:12]" "f[14:17]";
	setAttr ".iog[0].og[1].gcl" -type "componentList" 1 "f[13]";
	setAttr ".iog[0].og[2].gcl" -type "componentList" 2 "f[3]" "f[9]";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".pv" -type "double2" 0.47390708327293396 0.34093409031629562 ;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 72 ".uvst[0].uvsp[0:71]" -type "float2" 0.0018851225 0.0019920319
		 0.31539121 0.0019920319 0.31539121 0.33904546 0.0018851225 0.33904546 0.63681054
		 0.33904546 0.32298732 0.33904546 0.32298732 0.0019920319 0.63681054 0.0019920319
		 0.30519757 0.3428227 0.30519757 0.67987615 0.3008737 0.67987615 0.3008737 0.3428227
		 0.29106086 0.67987615 0.29106086 0.3428227 0.29506761 0.3428227 0.29506761 0.67987615
		 0.64390504 0.99800789 0.64390504 0.68365341 0.64822888 0.68365341 0.64822888 0.99800789
		 0.65497112 0.99800789 0.65497106 0.68365341 0.65929496 0.68365341 0.65929496 0.99800789
		 0.670371 0.68365347 0.670371 0.9974767 0.66603726 0.9971596 0.6660471 0.68365347
		 0.67711318 0.9974767 0.67710334 0.68397057 0.68143708 0.68365347 0.68143708 0.9974767
		 0.68848658 0.99746686 0.68816948 0.68365347 0.69249332 0.68365347 0.69249332 0.9974767
		 0.69923556 0.99747664 0.69923556 0.68365347 0.70355946 0.68365347 0.7032423 0.9974668
		 -2.61992884 -2.52485943 3.57378197 -2.52485943 3.57378197 3.67933512 -2.61992884
		 3.67933512 0.32298729 0.68365341 0.63681054 0.68365341 0.63681054 0.99800789 0.32298729
		 0.99800789 0.64823878 0.0019920319 0.64823878 0.33904546 0.64390504 0.33904546 0.64390504
		 0.0019920319 0.65929496 0.0019920631 0.65929496 0.33904546 0.65497106 0.33904546
		 0.65497106 0.0019920631 0.63062304 0.3428227 0.94444627 0.3428227 0.94444627 0.67987615
		 0.63062304 0.67987615 0.31100363 0.34282273 0.62481707 0.34282273 0.62481707 0.67987615
		 0.31100363 0.67987615 0.71030176 0.9974767 0.71030176 0.68365341 0.71462566 0.68365341
		 0.71462566 0.9974767 0.72136784 0.99747676 0.72136784 0.68365347 0.72569174 0.68365347
		 0.72569174 0.99747676;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 16 ".pt";
	setAttr ".pt[14]" -type "float3" 0 4.7683716e-06 0 ;
	setAttr ".pt[15]" -type "float3" 0 6.6757202e-06 0 ;
	setAttr ".pt[16]" -type "float3" 0 6.6757202e-06 0 ;
	setAttr ".pt[17]" -type "float3" 0 6.6757202e-06 0 ;
	setAttr ".pt[18]" -type "float3" 0 6.6757202e-06 0 ;
	setAttr ".pt[19]" -type "float3" 0 6.6757202e-06 0 ;
	setAttr ".pt[20]" -type "float3" 0 6.6757202e-06 0 ;
	setAttr ".pt[21]" -type "float3" 0 6.6757202e-06 0 ;
	setAttr ".pt[32]" -type "float3" 0 -1.9073486e-06 0 ;
	setAttr ".pt[33]" -type "float3" 0 -1.9073486e-06 0 ;
	setAttr ".pt[34]" -type "float3" 0 -1.9073486e-06 0 ;
	setAttr ".pt[35]" -type "float3" 0 -1.9073486e-06 0 ;
	setAttr ".pt[36]" -type "float3" 0 -1.9073486e-06 0 ;
	setAttr ".pt[37]" -type "float3" 0 -1.9073486e-06 0 ;
	setAttr ".pt[38]" -type "float3" 0 1.9073486e-06 0 ;
	setAttr ".pt[39]" -type "float3" 0 1.9073486e-06 0 ;
	setAttr -s 32 ".vt[0:31]"  -8.71151733 -0.059006691 -8.34357834 -8.71151733 -0.059006691 9.49800491
		 -8.95734024 -0.059006691 -8.34357834 -8.957901 -0.059006691 9.4799757 -8.95734024 19.10326767 -8.34357834
		 -8.957901 19.10326767 9.4799757 -8.71151733 19.10326767 -8.34357834 -8.71151733 19.10326767 9.49800491
		 8.88312054 -0.059006691 9.46194649 -8.95846081 -0.059006691 9.70776939 8.88312054 -0.059006691 9.70776939
		 -8.95846081 19.10326767 9.70776939 8.88312054 19.10326767 9.70776939 8.88312054 19.10326767 9.46194649
		 -8.92079163 -0.12290144 9.5811367 8.92079163 -0.12289762 9.5811367 -8.92079163 0.12292433 9.5811367
		 8.92079163 0.12292433 9.5811367 -8.92079163 0.12292433 -8.29064751 8.92079163 0.12292433 -8.29064751
		 -8.92079163 -0.12289762 -8.29064751 8.92079163 -0.12289762 -8.29064751 -8.957901 -0.059006691 9.4799757
		 -8.957901 -0.059006691 9.4799757 -8.957901 -0.059006691 9.4799757 -8.957901 -0.059006691 9.4799757
		 -8.957901 -0.059006691 9.4799757 -8.957901 19.10326767 9.4799757 -8.957901 19.10326767 9.4799757
		 -8.957901 19.10326767 9.4799757 -8.957901 19.10326767 9.4799757 -8.957901 19.10326767 9.4799757;
	setAttr -s 46 ".ed[0:45]"  0 1 0 2 26 0 4 31 0 6 7 0 0 2 0 1 25 0 2 4 0
		 3 5 0 4 6 0 30 7 0 6 0 0 7 1 0 23 8 0 9 10 0 11 12 0 27 13 0 3 9 0 8 10 0 9 11 0
		 10 12 0 11 5 0 12 13 0 13 8 0 14 15 0 16 17 0 18 19 0 20 21 0 14 16 0 15 17 0 16 18 0
		 17 19 0 18 20 0 19 21 0 20 14 0 21 15 0 22 9 0 22 8 0 24 31 0 23 28 0 25 30 0 1 26 0
		 2 24 0 11 27 0 28 13 0 29 7 0 4 29 0;
	setAttr -s 18 -ch 72 ".fc[0:17]" -type "polyFaces" 
		f 4 0 40 -2 -5
		mu 0 4 24 25 26 27
		f 4 41 37 -3 -7
		mu 0 4 0 1 2 3
		f 4 45 44 -4 -9
		mu 0 4 28 29 30 31
		f 4 3 11 -1 -11
		mu 0 4 4 5 6 7
		f 4 -12 -10 -40 -6
		mu 0 4 48 49 50 51
		f 4 10 4 6 8
		mu 0 4 52 53 54 55
		f 4 36 17 -14 -36
		mu 0 4 32 33 34 35
		f 4 13 19 -15 -19
		mu 0 4 56 57 58 59
		f 4 14 21 -16 -43
		mu 0 4 36 37 38 39
		f 4 43 22 -13 38
		mu 0 4 60 61 62 63
		f 4 -23 -22 -20 -18
		mu 0 4 8 9 10 11
		f 4 -8 16 18 20
		mu 0 4 12 13 14 15
		f 4 23 28 -25 -28
		mu 0 4 64 65 66 67
		f 4 24 30 -26 -30
		mu 0 4 40 41 42 43
		f 4 25 32 -27 -32
		mu 0 4 68 69 70 71
		f 4 26 34 -24 -34
		mu 0 4 44 45 46 47
		f 4 -35 -33 -31 -29
		mu 0 4 16 17 18 19
		f 4 33 27 29 31
		mu 0 4 20 21 22 23;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".pd[0]" -type "dataPolyComponent" Index_Data UV 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".ai_translator" -type "string" "polymesh";
createNode mesh -n "pasted__polySurfaceShape4" -p "pasted__room1";
	rename -uid "5CAD32FA-4B33-90D9-42CC-618256BCAB46";
	setAttr -k off ".v";
	setAttr ".io" yes;
	setAttr ".iog[0].og[0].gcl" -type "componentList" 1 "f[0:17]";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".pv" -type "double2" 0.5 0.875 ;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 42 ".uvst[0].uvsp[0:41]" -type "float2" 0.375 0 0.625 0 0.375
		 0.25 0.625 0.25 0.375 0.5 0.625 0.5 0.375 0.75 0.625 0.75 0.375 1 0.625 1 0.875 0
		 0.875 0.25 0.125 0 0.125 0.25 0.375 0 0.625 0 0.625 0.25 0.375 0.25 0.625 0.5 0.375
		 0.5 0.625 0.75 0.375 0.75 0.625 1 0.375 1 0.875 0 0.875 0.25 0.125 0 0.125 0.25 0.375
		 0 0.625 0 0.625 0.25 0.375 0.25 0.625 0.5 0.375 0.5 0.625 0.75 0.375 0.75 0.625 1
		 0.375 1 0.875 0 0.875 0.25 0.125 0 0.125 0.25;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 22 ".vt[0:21]"  -8.71151733 -0.059006691 -8.34357834 -8.71151733 -0.059006691 9.49800491
		 -8.95734024 -0.059006691 -8.34357834 -8.957901 -0.059006691 9.4799757 -8.95734024 19.10326767 -8.34357834
		 -8.957901 19.10326767 9.4799757 -8.71151733 19.10326767 -8.34357834 -8.71151733 19.10326767 9.49800491
		 8.88312054 -0.059006691 9.46194649 -8.95846081 -0.059006691 9.70776939 8.88312054 -0.059006691 9.70776939
		 -8.95846081 19.10326767 9.70776939 8.88312054 19.10326767 9.70776939 8.88312054 19.10326767 9.46194649
		 -8.92079163 -0.12291098 9.5811367 8.92079163 -0.12291098 9.5811367 -8.92079163 0.12291098 9.5811367
		 8.92079163 0.12291098 9.5811367 -8.92079163 0.12291098 -8.29064751 8.92079163 0.12291098 -8.29064751
		 -8.92079163 -0.12291098 -8.29064751 8.92079163 -0.12291098 -8.29064751;
	setAttr -s 35 ".ed[0:34]"  0 1 0 2 3 0 4 5 0 6 7 0 0 2 0 1 3 0 2 4 0
		 3 5 0 4 6 0 5 7 0 6 0 0 7 1 0 3 8 0 9 10 0 11 12 0 5 13 0 3 9 0 8 10 0 9 11 0 10 12 0
		 11 5 0 12 13 0 13 8 0 14 15 0 16 17 0 18 19 0 20 21 0 14 16 0 15 17 0 16 18 0 17 19 0
		 18 20 0 19 21 0 20 14 0 21 15 0;
	setAttr -s 18 -ch 72 ".fc[0:17]" -type "polyFaces" 
		f 4 0 5 -2 -5
		mu 0 4 0 1 3 2
		f 4 1 7 -3 -7
		mu 0 4 2 3 5 4
		f 4 2 9 -4 -9
		mu 0 4 4 5 7 6
		f 4 3 11 -1 -11
		mu 0 4 6 7 9 8
		f 4 -12 -10 -8 -6
		mu 0 4 1 10 11 3
		f 4 10 4 6 8
		mu 0 4 12 0 2 13
		f 4 12 17 -14 -17
		mu 0 4 14 15 16 17
		f 4 13 19 -15 -19
		mu 0 4 17 16 18 19
		f 4 14 21 -16 -21
		mu 0 4 19 18 20 21
		f 4 15 22 -13 7
		mu 0 4 21 20 22 23
		f 4 -23 -22 -20 -18
		mu 0 4 15 24 25 16
		f 4 -8 16 18 20
		mu 0 4 26 14 17 27
		f 4 23 28 -25 -28
		mu 0 4 28 29 30 31
		f 4 24 30 -26 -30
		mu 0 4 31 30 32 33
		f 4 25 32 -27 -32
		mu 0 4 33 32 34 35
		f 4 26 34 -24 -34
		mu 0 4 35 34 36 37
		f 4 -35 -33 -31 -29
		mu 0 4 29 38 39 30
		f 4 33 27 29 31
		mu 0 4 40 28 31 41;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".pd[0]" -type "dataPolyComponent" Index_Data UV 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".ai_translator" -type "string" "polymesh";
createNode mesh -n "pasted__polySurfaceShape5" -p "pasted__room1";
	rename -uid "B83361BA-4778-312C-A72F-36BB1A48315C";
	setAttr -k off ".v";
	setAttr ".io" yes;
	setAttr ".iog[0].og[0].gcl" -type "componentList" 1 "f[0:17]";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".pv" -type "double2" 0.47330814599990845 0.5519372932612896 ;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 56 ".uvst[0].uvsp[0:55]" -type "float2" 1.27764034 0.52767682
		 -0.27513993 0.52658415 -0.48030692 0.53899884 0.38180965 0.50676888 0.3115086 0.66321784
		 0.64477146 0.60120457 0.37811229 1.021149874 0.71137512 0.95913661 1.76444638 -0.30287877
		 -0.76697236 -0.30390608 -0.77764034 -0.27767682 1.31692803 0.54480916 0.57190329
		 0.11428401 0.57420897 0.14326733 1.30664682 0.57005346 0.64205676 0.65143728 0.30987534
		 0.58346975 0.61828274 0.74332249 0.62290615 1.0023729801 2.83119845 -0.065445714
		 2.8335042 -0.036462396 -0.80664688 -0.32005346 -0.81692809 -0.2948091 0.26083252
		 0.16717252 0.68514895 0.12109531 0.6857838 0.12694156 0.26146737 0.17301877 0.73193902
		 0.55197626 0.30762258 0.59805346 0.73257387 0.55782253 0.30825743 0.60389972 0.77872908
		 0.98285723 0.35441262 1.028934479 1.11018372 0.074940108 1.11081851 0.080786347 -0.16420221
		 0.21332772 -0.16356736 0.21917397 -1.53144264 0.28374693 0.38171723 1.0066775084
		 -0.26444638 0.55287874 0.61819035 0.24323115 1.49036264 -0.26138377 0.30901796 0.587713
		 0.37709388 0.74762708 1.77513993 -0.27658415 0.64357829 0.59666502 0.62287933 0.50240749
		 0.31065419 0.65862614 0.64112031 0.65601414 1.26697242 0.55390608 0.37712067 0.24759254
		 1.48129106 -0.28943467 0.3828741 0.22669911 -1.5293721 0.31060982 0.71505553 0.29466671
		 -0.49134672 0.51181966;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 16 ".pt";
	setAttr ".pt[14]" -type "float3" 0 4.7683716e-06 0 ;
	setAttr ".pt[15]" -type "float3" 0 6.6757202e-06 0 ;
	setAttr ".pt[16]" -type "float3" 0 6.6757202e-06 0 ;
	setAttr ".pt[17]" -type "float3" 0 6.6757202e-06 0 ;
	setAttr ".pt[18]" -type "float3" 0 6.6757202e-06 0 ;
	setAttr ".pt[19]" -type "float3" 0 6.6757202e-06 0 ;
	setAttr ".pt[20]" -type "float3" 0 6.6757202e-06 0 ;
	setAttr ".pt[21]" -type "float3" 0 6.6757202e-06 0 ;
	setAttr ".pt[32]" -type "float3" 0 -1.9073486e-06 0 ;
	setAttr ".pt[33]" -type "float3" 0 -1.9073486e-06 0 ;
	setAttr ".pt[34]" -type "float3" 0 -1.9073486e-06 0 ;
	setAttr ".pt[35]" -type "float3" 0 -1.9073486e-06 0 ;
	setAttr ".pt[36]" -type "float3" 0 -1.9073486e-06 0 ;
	setAttr ".pt[37]" -type "float3" 0 -1.9073486e-06 0 ;
	setAttr ".pt[38]" -type "float3" 0 1.9073486e-06 0 ;
	setAttr ".pt[39]" -type "float3" 0 1.9073486e-06 0 ;
	setAttr -s 32 ".vt[0:31]"  -8.71151733 -0.059006691 -8.34357834 -8.71151733 -0.059006691 9.49800491
		 -8.95734024 -0.059006691 -8.34357834 -8.957901 -0.059006691 9.4799757 -8.95734024 19.10326767 -8.34357834
		 -8.957901 19.10326767 9.4799757 -8.71151733 19.10326767 -8.34357834 -8.71151733 19.10326767 9.49800491
		 8.88312054 -0.059006691 9.46194649 -8.95846081 -0.059006691 9.70776939 8.88312054 -0.059006691 9.70776939
		 -8.95846081 19.10326767 9.70776939 8.88312054 19.10326767 9.70776939 8.88312054 19.10326767 9.46194649
		 -8.92079163 -0.12290621 9.5811367 8.92079163 -0.1229043 9.5811367 -8.92079163 0.12291765 9.5811367
		 8.92079163 0.12291765 9.5811367 -8.92079163 0.12291765 -8.29064751 8.92079163 0.12291765 -8.29064751
		 -8.92079163 -0.1229043 -8.29064751 8.92079163 -0.1229043 -8.29064751 -8.957901 -0.059006691 9.4799757
		 -8.957901 -0.059006691 9.4799757 -8.957901 -0.059006691 9.4799757 -8.957901 -0.059006691 9.4799757
		 -8.957901 -0.059006691 9.4799757 -8.957901 19.10326767 9.4799757 -8.957901 19.10326767 9.4799757
		 -8.957901 19.10326767 9.4799757 -8.957901 19.10326767 9.4799757 -8.957901 19.10326767 9.4799757;
	setAttr -s 46 ".ed[0:45]"  0 1 0 2 26 0 4 31 0 6 7 0 0 2 0 1 25 0 2 4 0
		 3 5 0 4 6 0 30 7 0 6 0 0 7 1 0 23 8 0 9 10 0 11 12 0 27 13 0 3 9 0 8 10 0 9 11 0
		 10 12 0 11 5 0 12 13 0 13 8 0 14 15 0 16 17 0 18 19 0 20 21 0 14 16 0 15 17 0 16 18 0
		 17 19 0 18 20 0 19 21 0 20 14 0 21 15 0 22 9 0 22 8 0 24 31 0 23 28 0 25 30 0 1 26 0
		 2 24 0 11 27 0 28 13 0 29 7 0 4 29 0;
	setAttr -s 18 -ch 72 ".fc[0:17]" -type "polyFaces" 
		f 4 0 40 -2 -5
		mu 0 4 55 51 41 2
		f 4 41 37 -3 -7
		mu 0 4 50 40 46 3
		f 4 45 44 -4 -9
		mu 0 4 47 45 5 4
		f 4 3 11 -1 -11
		mu 0 4 4 5 7 6
		f 4 -12 -10 -40 -6
		mu 0 4 1 8 44 39
		f 4 10 4 6 8
		mu 0 4 9 0 49 10
		f 4 36 17 -14 -36
		mu 0 4 37 12 13 53
		f 4 13 19 -15 -19
		mu 0 4 52 54 15 16
		f 4 14 21 -16 -43
		mu 0 4 16 15 48 42
		f 4 43 22 -13 38
		mu 0 4 43 17 18 38
		f 4 -23 -22 -20 -18
		mu 0 4 12 19 20 13
		f 4 -8 16 18 20
		mu 0 4 21 11 14 22
		f 4 23 28 -25 -28
		mu 0 4 23 24 25 26
		f 4 24 30 -26 -30
		mu 0 4 26 25 27 28
		f 4 25 32 -27 -32
		mu 0 4 28 27 29 30
		f 4 26 34 -24 -34
		mu 0 4 30 29 31 32
		f 4 -35 -33 -31 -29
		mu 0 4 24 33 34 25
		f 4 33 27 29 31
		mu 0 4 35 23 26 36;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".pd[0]" -type "dataPolyComponent" Index_Data UV 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".ai_translator" -type "string" "polymesh";
createNode transform -n "pasted__room" -p "ROOM";
	rename -uid "2EDA97DB-4735-7977-EF17-9BBE0BCCE296";
	setAttr ".t" -type "double3" -3.4942773185150591 10.724690540241639 12.198117849776478 ;
	setAttr ".s" -type "double3" 1.6620864049942878 1.2463779114912545 1.5430197509225698 ;
	setAttr ".rp" -type "double3" 0.91805295755752014 -9.4356098741389935 -7.7832937129483115 ;
	setAttr ".sp" -type "double3" -0.37452560925093292 0.55492509528688461 -2.9021995422162101 ;
	setAttr ".spt" -type "double3" 1.2925785668084389 -9.9905349694259318 -4.8810941707320907 ;
createNode mesh -n "pasted__roomShape" -p "pasted__room";
	rename -uid "E5F797F5-4C3A-8D5B-A064-9C9ECD7823F0";
	setAttr -k off ".v";
	setAttr -s 6 ".iog[0].og";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".pv" -type "double2" 0.47390708327293396 0.34093409031629562 ;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 16 ".pt";
	setAttr ".pt[14]" -type "float3" 0 4.7683716e-06 0 ;
	setAttr ".pt[15]" -type "float3" 0 6.6757202e-06 0 ;
	setAttr ".pt[16]" -type "float3" 0 6.6757202e-06 0 ;
	setAttr ".pt[17]" -type "float3" 0 6.6757202e-06 0 ;
	setAttr ".pt[18]" -type "float3" 0 6.6757202e-06 0 ;
	setAttr ".pt[19]" -type "float3" 0 6.6757202e-06 0 ;
	setAttr ".pt[20]" -type "float3" 0 6.6757202e-06 0 ;
	setAttr ".pt[21]" -type "float3" 0 6.6757202e-06 0 ;
	setAttr ".pt[32]" -type "float3" 0 -1.9073486e-06 0 ;
	setAttr ".pt[33]" -type "float3" 0 -1.9073486e-06 0 ;
	setAttr ".pt[34]" -type "float3" 0 -1.9073486e-06 0 ;
	setAttr ".pt[35]" -type "float3" 0 -1.9073486e-06 0 ;
	setAttr ".pt[36]" -type "float3" 0 -1.9073486e-06 0 ;
	setAttr ".pt[37]" -type "float3" 0 -1.9073486e-06 0 ;
	setAttr ".pt[38]" -type "float3" 0 1.9073486e-06 0 ;
	setAttr ".pt[39]" -type "float3" 0 1.9073486e-06 0 ;
	setAttr ".ai_translator" -type "string" "polymesh";
createNode mesh -n "pasted__polySurfaceShape4" -p "pasted__room";
	rename -uid "F971E863-4129-B60E-523E-45B0D15BA67E";
	setAttr -k off ".v";
	setAttr ".io" yes;
	setAttr ".iog[0].og[0].gcl" -type "componentList" 1 "f[0:17]";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".pv" -type "double2" 0.5 0.875 ;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 42 ".uvst[0].uvsp[0:41]" -type "float2" 0.375 0 0.625 0 0.375
		 0.25 0.625 0.25 0.375 0.5 0.625 0.5 0.375 0.75 0.625 0.75 0.375 1 0.625 1 0.875 0
		 0.875 0.25 0.125 0 0.125 0.25 0.375 0 0.625 0 0.625 0.25 0.375 0.25 0.625 0.5 0.375
		 0.5 0.625 0.75 0.375 0.75 0.625 1 0.375 1 0.875 0 0.875 0.25 0.125 0 0.125 0.25 0.375
		 0 0.625 0 0.625 0.25 0.375 0.25 0.625 0.5 0.375 0.5 0.625 0.75 0.375 0.75 0.625 1
		 0.375 1 0.875 0 0.875 0.25 0.125 0 0.125 0.25;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 22 ".vt[0:21]"  -8.71151733 -0.059006691 -8.34357834 -8.71151733 -0.059006691 9.49800491
		 -8.95734024 -0.059006691 -8.34357834 -8.957901 -0.059006691 9.4799757 -8.95734024 19.10326767 -8.34357834
		 -8.957901 19.10326767 9.4799757 -8.71151733 19.10326767 -8.34357834 -8.71151733 19.10326767 9.49800491
		 8.88312054 -0.059006691 9.46194649 -8.95846081 -0.059006691 9.70776939 8.88312054 -0.059006691 9.70776939
		 -8.95846081 19.10326767 9.70776939 8.88312054 19.10326767 9.70776939 8.88312054 19.10326767 9.46194649
		 -8.92079163 -0.12291098 9.5811367 8.92079163 -0.12291098 9.5811367 -8.92079163 0.12291098 9.5811367
		 8.92079163 0.12291098 9.5811367 -8.92079163 0.12291098 -8.29064751 8.92079163 0.12291098 -8.29064751
		 -8.92079163 -0.12291098 -8.29064751 8.92079163 -0.12291098 -8.29064751;
	setAttr -s 35 ".ed[0:34]"  0 1 0 2 3 0 4 5 0 6 7 0 0 2 0 1 3 0 2 4 0
		 3 5 0 4 6 0 5 7 0 6 0 0 7 1 0 3 8 0 9 10 0 11 12 0 5 13 0 3 9 0 8 10 0 9 11 0 10 12 0
		 11 5 0 12 13 0 13 8 0 14 15 0 16 17 0 18 19 0 20 21 0 14 16 0 15 17 0 16 18 0 17 19 0
		 18 20 0 19 21 0 20 14 0 21 15 0;
	setAttr -s 18 -ch 72 ".fc[0:17]" -type "polyFaces" 
		f 4 0 5 -2 -5
		mu 0 4 0 1 3 2
		f 4 1 7 -3 -7
		mu 0 4 2 3 5 4
		f 4 2 9 -4 -9
		mu 0 4 4 5 7 6
		f 4 3 11 -1 -11
		mu 0 4 6 7 9 8
		f 4 -12 -10 -8 -6
		mu 0 4 1 10 11 3
		f 4 10 4 6 8
		mu 0 4 12 0 2 13
		f 4 12 17 -14 -17
		mu 0 4 14 15 16 17
		f 4 13 19 -15 -19
		mu 0 4 17 16 18 19
		f 4 14 21 -16 -21
		mu 0 4 19 18 20 21
		f 4 15 22 -13 7
		mu 0 4 21 20 22 23
		f 4 -23 -22 -20 -18
		mu 0 4 15 24 25 16
		f 4 -8 16 18 20
		mu 0 4 26 14 17 27
		f 4 23 28 -25 -28
		mu 0 4 28 29 30 31
		f 4 24 30 -26 -30
		mu 0 4 31 30 32 33
		f 4 25 32 -27 -32
		mu 0 4 33 32 34 35
		f 4 26 34 -24 -34
		mu 0 4 35 34 36 37
		f 4 -35 -33 -31 -29
		mu 0 4 29 38 39 30
		f 4 33 27 29 31
		mu 0 4 40 28 31 41;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".pd[0]" -type "dataPolyComponent" Index_Data UV 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".ai_translator" -type "string" "polymesh";
createNode mesh -n "pasted__polySurfaceShape5" -p "pasted__room";
	rename -uid "41918D29-49AD-2158-A8F7-8BAE1F83BE4C";
	setAttr -k off ".v";
	setAttr ".io" yes;
	setAttr ".iog[0].og[0].gcl" -type "componentList" 1 "f[0:17]";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".pv" -type "double2" 0.47330814599990845 0.5519372932612896 ;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 56 ".uvst[0].uvsp[0:55]" -type "float2" 1.27764034 0.52767682
		 -0.27513993 0.52658415 -0.48030692 0.53899884 0.38180965 0.50676888 0.3115086 0.66321784
		 0.64477146 0.60120457 0.37811229 1.021149874 0.71137512 0.95913661 1.76444638 -0.30287877
		 -0.76697236 -0.30390608 -0.77764034 -0.27767682 1.31692803 0.54480916 0.57190329
		 0.11428401 0.57420897 0.14326733 1.30664682 0.57005346 0.64205676 0.65143728 0.30987534
		 0.58346975 0.61828274 0.74332249 0.62290615 1.0023729801 2.83119845 -0.065445714
		 2.8335042 -0.036462396 -0.80664688 -0.32005346 -0.81692809 -0.2948091 0.26083252
		 0.16717252 0.68514895 0.12109531 0.6857838 0.12694156 0.26146737 0.17301877 0.73193902
		 0.55197626 0.30762258 0.59805346 0.73257387 0.55782253 0.30825743 0.60389972 0.77872908
		 0.98285723 0.35441262 1.028934479 1.11018372 0.074940108 1.11081851 0.080786347 -0.16420221
		 0.21332772 -0.16356736 0.21917397 -1.53144264 0.28374693 0.38171723 1.0066775084
		 -0.26444638 0.55287874 0.61819035 0.24323115 1.49036264 -0.26138377 0.30901796 0.587713
		 0.37709388 0.74762708 1.77513993 -0.27658415 0.64357829 0.59666502 0.62287933 0.50240749
		 0.31065419 0.65862614 0.64112031 0.65601414 1.26697242 0.55390608 0.37712067 0.24759254
		 1.48129106 -0.28943467 0.3828741 0.22669911 -1.5293721 0.31060982 0.71505553 0.29466671
		 -0.49134672 0.51181966;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 16 ".pt";
	setAttr ".pt[14]" -type "float3" 0 4.7683716e-06 0 ;
	setAttr ".pt[15]" -type "float3" 0 6.6757202e-06 0 ;
	setAttr ".pt[16]" -type "float3" 0 6.6757202e-06 0 ;
	setAttr ".pt[17]" -type "float3" 0 6.6757202e-06 0 ;
	setAttr ".pt[18]" -type "float3" 0 6.6757202e-06 0 ;
	setAttr ".pt[19]" -type "float3" 0 6.6757202e-06 0 ;
	setAttr ".pt[20]" -type "float3" 0 6.6757202e-06 0 ;
	setAttr ".pt[21]" -type "float3" 0 6.6757202e-06 0 ;
	setAttr ".pt[32]" -type "float3" 0 -1.9073486e-06 0 ;
	setAttr ".pt[33]" -type "float3" 0 -1.9073486e-06 0 ;
	setAttr ".pt[34]" -type "float3" 0 -1.9073486e-06 0 ;
	setAttr ".pt[35]" -type "float3" 0 -1.9073486e-06 0 ;
	setAttr ".pt[36]" -type "float3" 0 -1.9073486e-06 0 ;
	setAttr ".pt[37]" -type "float3" 0 -1.9073486e-06 0 ;
	setAttr ".pt[38]" -type "float3" 0 1.9073486e-06 0 ;
	setAttr ".pt[39]" -type "float3" 0 1.9073486e-06 0 ;
	setAttr -s 32 ".vt[0:31]"  -8.71151733 -0.059006691 -8.34357834 -8.71151733 -0.059006691 9.49800491
		 -8.95734024 -0.059006691 -8.34357834 -8.957901 -0.059006691 9.4799757 -8.95734024 19.10326767 -8.34357834
		 -8.957901 19.10326767 9.4799757 -8.71151733 19.10326767 -8.34357834 -8.71151733 19.10326767 9.49800491
		 8.88312054 -0.059006691 9.46194649 -8.95846081 -0.059006691 9.70776939 8.88312054 -0.059006691 9.70776939
		 -8.95846081 19.10326767 9.70776939 8.88312054 19.10326767 9.70776939 8.88312054 19.10326767 9.46194649
		 -8.92079163 -0.12290621 9.5811367 8.92079163 -0.1229043 9.5811367 -8.92079163 0.12291765 9.5811367
		 8.92079163 0.12291765 9.5811367 -8.92079163 0.12291765 -8.29064751 8.92079163 0.12291765 -8.29064751
		 -8.92079163 -0.1229043 -8.29064751 8.92079163 -0.1229043 -8.29064751 -8.957901 -0.059006691 9.4799757
		 -8.957901 -0.059006691 9.4799757 -8.957901 -0.059006691 9.4799757 -8.957901 -0.059006691 9.4799757
		 -8.957901 -0.059006691 9.4799757 -8.957901 19.10326767 9.4799757 -8.957901 19.10326767 9.4799757
		 -8.957901 19.10326767 9.4799757 -8.957901 19.10326767 9.4799757 -8.957901 19.10326767 9.4799757;
	setAttr -s 46 ".ed[0:45]"  0 1 0 2 26 0 4 31 0 6 7 0 0 2 0 1 25 0 2 4 0
		 3 5 0 4 6 0 30 7 0 6 0 0 7 1 0 23 8 0 9 10 0 11 12 0 27 13 0 3 9 0 8 10 0 9 11 0
		 10 12 0 11 5 0 12 13 0 13 8 0 14 15 0 16 17 0 18 19 0 20 21 0 14 16 0 15 17 0 16 18 0
		 17 19 0 18 20 0 19 21 0 20 14 0 21 15 0 22 9 0 22 8 0 24 31 0 23 28 0 25 30 0 1 26 0
		 2 24 0 11 27 0 28 13 0 29 7 0 4 29 0;
	setAttr -s 18 -ch 72 ".fc[0:17]" -type "polyFaces" 
		f 4 0 40 -2 -5
		mu 0 4 55 51 41 2
		f 4 41 37 -3 -7
		mu 0 4 50 40 46 3
		f 4 45 44 -4 -9
		mu 0 4 47 45 5 4
		f 4 3 11 -1 -11
		mu 0 4 4 5 7 6
		f 4 -12 -10 -40 -6
		mu 0 4 1 8 44 39
		f 4 10 4 6 8
		mu 0 4 9 0 49 10
		f 4 36 17 -14 -36
		mu 0 4 37 12 13 53
		f 4 13 19 -15 -19
		mu 0 4 52 54 15 16
		f 4 14 21 -16 -43
		mu 0 4 16 15 48 42
		f 4 43 22 -13 38
		mu 0 4 43 17 18 38
		f 4 -23 -22 -20 -18
		mu 0 4 12 19 20 13
		f 4 -8 16 18 20
		mu 0 4 21 11 14 22
		f 4 23 28 -25 -28
		mu 0 4 23 24 25 26
		f 4 24 30 -26 -30
		mu 0 4 26 25 27 28
		f 4 25 32 -27 -32
		mu 0 4 28 27 29 30
		f 4 26 34 -24 -34
		mu 0 4 30 29 31 32
		f 4 -35 -33 -31 -29
		mu 0 4 24 33 34 25
		f 4 33 27 29 31
		mu 0 4 35 23 26 36;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".pd[0]" -type "dataPolyComponent" Index_Data UV 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".ai_translator" -type "string" "polymesh";
createNode transform -n "group";
	rename -uid "457FF202-4B9E-074C-48EE-ACAD38B2FEBD";
	setAttr ".rp" -type "double3" -1.9850351549976146 12.518000108905115 10.921307025590888 ;
	setAttr ".sp" -type "double3" -1.9850351549976146 12.518000108905115 10.921307025590888 ;
createNode lightLinker -s -n "lightLinker1";
	rename -uid "D6908982-4CE2-7A48-EC08-5BB0535AF0CA";
	setAttr -s 4 ".lnk";
	setAttr -s 4 ".slnk";
createNode shapeEditorManager -n "shapeEditorManager";
	rename -uid "CBED353D-4740-F440-E55D-5AB3D0AFE980";
createNode poseInterpolatorManager -n "poseInterpolatorManager";
	rename -uid "0BCA523F-49EF-9F6D-1E09-C09EC2CDC25B";
createNode displayLayerManager -n "layerManager";
	rename -uid "6C77B7DF-4F8A-7821-6869-488FF111BEB7";
createNode displayLayer -n "defaultLayer";
	rename -uid "EFC5A118-4666-186E-C770-6FAEDEC0C63D";
createNode renderLayerManager -n "renderLayerManager";
	rename -uid "CC952575-454D-F910-7368-6BB828A6E79B";
createNode renderLayer -n "defaultRenderLayer";
	rename -uid "0D12E985-4619-78B6-C57F-C9820EF42354";
	setAttr ".g" yes;
createNode groupId -n "pasted__groupId28";
	rename -uid "D60657F3-4E98-4C55-9C4A-E3922299E88C";
	setAttr ".ihi" 0;
createNode groupId -n "pasted__groupId29";
	rename -uid "DC5DE3F5-4DE5-E347-9896-0493732EBB76";
	setAttr ".ihi" 0;
createNode shadingEngine -n "pasted__lambert2SG";
	rename -uid "EEBC4456-4D39-D1B8-E447-D1A7A8DDB4A4";
	setAttr ".ihi" 0;
	setAttr -s 2 ".dsm";
	setAttr ".ro" yes;
	setAttr -s 2 ".gn";
createNode materialInfo -n "pasted__materialInfo3";
	rename -uid "063AA9F4-4875-D530-E72A-4B8DB316DE42";
createNode lambert -n "pasted__lambert2";
	rename -uid "BD27413D-4D84-B436-ED68-0AA607C2B211";
createNode file -n "pasted__file4";
	rename -uid "D2E311F4-4EA7-4C64-27B1-049D99CB8965";
	setAttr ".ftn" -type "string" "G:/Work Folder/Development/HackthonTeenHaxTX/resources/flooring_tileB2.png";
	setAttr ".cs" -type "string" "sRGB";
createNode place2dTexture -n "pasted__place2dTexture4";
	rename -uid "5F124CE8-443B-E710-2920-4BB84CBD0B84";
createNode groupId -n "pasted__groupId30";
	rename -uid "D296235F-4CF4-105E-5189-52984F4214B1";
	setAttr ".ihi" 0;
createNode shadingEngine -n "pasted__phong12SG";
	rename -uid "9D4267F9-4A98-85D9-ED63-D9A0FEDDD10E";
	setAttr ".ihi" 0;
	setAttr -s 2 ".dsm";
	setAttr ".ro" yes;
	setAttr -s 2 ".gn";
createNode materialInfo -n "pasted__materialInfo13";
	rename -uid "1AD66752-4F7A-BEB9-52AC-A98C32019C36";
createNode phong -n "pasted__phong12";
	rename -uid "398BA810-4D5C-3983-ED40-6FBA541D06F2";
createNode file -n "pasted__file13";
	rename -uid "DB9A9A0E-4227-1240-11CE-258F0A0FA8CA";
	setAttr ".ftn" -type "string" "G:/Work Folder/Development/HackthonTeenHaxTX/resources/a_blue.png";
	setAttr ".cs" -type "string" "sRGB";
createNode place2dTexture -n "pasted__place2dTexture13";
	rename -uid "409F7B38-44F9-4387-CACC-C299336715BC";
	setAttr ".re" -type "float2" 25 1 ;
createNode groupParts -n "pasted__groupParts16";
	rename -uid "1A7CE0DD-43D0-6EF4-95C0-C08F0F9FF620";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 2 "f[3]" "f[9]";
createNode polyTweakUV -n "pasted__polyTweakUV9";
	rename -uid "E0D59851-4D1C-2482-1273-1FB6B11275FF";
	setAttr ".uopa" yes;
	setAttr -s 5 ".uvtk";
	setAttr ".uvtk[40]" -type "float2" -2.621814 -3.2085128 ;
	setAttr ".uvtk[41]" -type "float2" 3.2580736 -3.2085128 ;
	setAttr ".uvtk[42]" -type "float2" 3.2580736 2.6813271 ;
	setAttr ".uvtk[43]" -type "float2" -2.621814 2.6813271 ;
createNode groupParts -n "pasted__groupParts12";
	rename -uid "EF89121A-42E7-078C-C11A-FBBDBFE4979F";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "f[13]";
createNode polyAutoProj -n "pasted__polyAutoProj6";
	rename -uid "B53AE08F-47CD-ABCF-DFDB-56899E6F3AE8";
	setAttr ".uopa" yes;
	setAttr ".ics" -type "componentList" 1 "f[0:17]";
	setAttr ".ix" -type "matrix" 1.6620864049942878 0 0 0 0 1.2463779114912545 0 0 0 0 1.5430197509225698 0
		 -1.9537304374993747 0.59743428480483929 8.8929753515862302 1;
	setAttr ".s" -type "double3" 29.716862401641542 29.716862401641542 29.716862401641542 ;
	setAttr ".ps" 0.20000000298023224;
	setAttr ".dl" yes;
createNode groupParts -n "pasted__groupParts9";
	rename -uid "E5E683F9-4B9C-48FE-7854-4E84926A9586";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 4 "f[0:2]" "f[4:8]" "f[10:12]" "f[14:17]";
	setAttr ".irc" -type "componentList" 3 "f[3]" "f[9]" "f[13]";
createNode groupId -n "pasted__groupId19";
	rename -uid "C2C773F6-462D-7732-F09A-C2944FBEAD08";
	setAttr ".ihi" 0;
createNode groupId -n "pasted__groupId21";
	rename -uid "EFA424BF-4A20-9A00-2F3C-5387A2E69C4D";
	setAttr ".ihi" 0;
createNode groupId -n "pasted__groupId27";
	rename -uid "32DEDE3B-4DA7-F192-2145-4190A52414A2";
	setAttr ".ihi" 0;
createNode script -n "uiConfigurationScriptNode";
	rename -uid "436E1705-4F1B-46B3-760C-55AEBAE702DA";
	setAttr ".b" -type "string" (
		"// Maya Mel UI Configuration File.\n//\n//  This script is machine generated.  Edit at your own risk.\n//\n//\n\nglobal string $gMainPane;\nif (`paneLayout -exists $gMainPane`) {\n\n\tglobal int $gUseScenePanelConfig;\n\tint    $useSceneConfig = $gUseScenePanelConfig;\n\tint    $nodeEditorPanelVisible = stringArrayContains(\"nodeEditorPanel1\", `getPanel -vis`);\n\tint    $nodeEditorWorkspaceControlOpen = (`workspaceControl -exists nodeEditorPanel1Window` && `workspaceControl -q -visible nodeEditorPanel1Window`);\n\tint    $menusOkayInPanels = `optionVar -q allowMenusInPanels`;\n\tint    $nVisPanes = `paneLayout -q -nvp $gMainPane`;\n\tint    $nPanes = 0;\n\tstring $editorName;\n\tstring $panelName;\n\tstring $itemFilterName;\n\tstring $panelConfig;\n\n\t//\n\t//  get current state of the UI\n\t//\n\tsceneUIReplacement -update $gMainPane;\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"modelPanel\" (localizedPanelLabel(\"Top View\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tmodelPanel -edit -l (localizedPanelLabel(\"Top View\")) -mbv $menusOkayInPanels  $panelName;\n"
		+ "\t\t$editorName = $panelName;\n        modelEditor -e \n            -camera \"top\" \n            -useInteractiveMode 0\n            -displayLights \"default\" \n            -displayAppearance \"smoothShaded\" \n            -activeOnly 0\n            -ignorePanZoom 0\n            -wireframeOnShaded 0\n            -headsUpDisplay 1\n            -holdOuts 1\n            -selectionHiliteDisplay 1\n            -useDefaultMaterial 0\n            -bufferMode \"double\" \n            -twoSidedLighting 0\n            -backfaceCulling 0\n            -xray 0\n            -jointXray 0\n            -activeComponentsXray 0\n            -displayTextures 0\n            -smoothWireframe 0\n            -lineWidth 1\n            -textureAnisotropic 0\n            -textureHilight 1\n            -textureSampling 2\n            -textureDisplay \"modulate\" \n            -textureMaxSize 32768\n            -fogging 0\n            -fogSource \"fragment\" \n            -fogMode \"linear\" \n            -fogStart 0\n            -fogEnd 100\n            -fogDensity 0.1\n            -fogColor 0.5 0.5 0.5 1 \n"
		+ "            -depthOfFieldPreview 1\n            -maxConstantTransparency 1\n            -rendererName \"vp2Renderer\" \n            -objectFilterShowInHUD 1\n            -isFiltered 0\n            -colorResolution 256 256 \n            -bumpResolution 512 512 \n            -textureCompression 0\n            -transparencyAlgorithm \"frontAndBackCull\" \n            -transpInShadows 0\n            -cullingOverride \"none\" \n            -lowQualityLighting 0\n            -maximumNumHardwareLights 1\n            -occlusionCulling 0\n            -shadingModel 0\n            -useBaseRenderer 0\n            -useReducedRenderer 0\n            -smallObjectCulling 0\n            -smallObjectThreshold -1 \n            -interactiveDisableShadows 0\n            -interactiveBackFaceCull 0\n            -sortTransparent 1\n            -controllers 1\n            -nurbsCurves 1\n            -nurbsSurfaces 1\n            -polymeshes 1\n            -subdivSurfaces 1\n            -planes 1\n            -lights 1\n            -cameras 1\n            -controlVertices 1\n"
		+ "            -hulls 1\n            -grid 1\n            -imagePlane 1\n            -joints 1\n            -ikHandles 1\n            -deformers 1\n            -dynamics 1\n            -particleInstancers 1\n            -fluids 1\n            -hairSystems 1\n            -follicles 1\n            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n            -locators 1\n            -manipulators 1\n            -pluginShapes 1\n            -dimensions 1\n            -handles 1\n            -pivots 1\n            -textures 1\n            -strokes 1\n            -motionTrails 1\n            -clipGhosts 1\n            -greasePencils 1\n            -shadows 0\n            -captureSequenceNumber -1\n            -width 1\n            -height 1\n            -sceneRenderFilter 0\n            $editorName;\n        modelEditor -e -viewSelected 0 $editorName;\n        modelEditor -e \n            -pluginObjects \"gpuCacheDisplayFilter\" 1 \n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n"
		+ "\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"modelPanel\" (localizedPanelLabel(\"Side View\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tmodelPanel -edit -l (localizedPanelLabel(\"Side View\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        modelEditor -e \n            -camera \"side\" \n            -useInteractiveMode 0\n            -displayLights \"default\" \n            -displayAppearance \"smoothShaded\" \n            -activeOnly 0\n            -ignorePanZoom 0\n            -wireframeOnShaded 0\n            -headsUpDisplay 1\n            -holdOuts 1\n            -selectionHiliteDisplay 1\n            -useDefaultMaterial 0\n            -bufferMode \"double\" \n            -twoSidedLighting 0\n            -backfaceCulling 0\n            -xray 0\n            -jointXray 0\n            -activeComponentsXray 0\n            -displayTextures 0\n            -smoothWireframe 0\n            -lineWidth 1\n            -textureAnisotropic 0\n            -textureHilight 1\n            -textureSampling 2\n"
		+ "            -textureDisplay \"modulate\" \n            -textureMaxSize 32768\n            -fogging 0\n            -fogSource \"fragment\" \n            -fogMode \"linear\" \n            -fogStart 0\n            -fogEnd 100\n            -fogDensity 0.1\n            -fogColor 0.5 0.5 0.5 1 \n            -depthOfFieldPreview 1\n            -maxConstantTransparency 1\n            -rendererName \"vp2Renderer\" \n            -objectFilterShowInHUD 1\n            -isFiltered 0\n            -colorResolution 256 256 \n            -bumpResolution 512 512 \n            -textureCompression 0\n            -transparencyAlgorithm \"frontAndBackCull\" \n            -transpInShadows 0\n            -cullingOverride \"none\" \n            -lowQualityLighting 0\n            -maximumNumHardwareLights 1\n            -occlusionCulling 0\n            -shadingModel 0\n            -useBaseRenderer 0\n            -useReducedRenderer 0\n            -smallObjectCulling 0\n            -smallObjectThreshold -1 \n            -interactiveDisableShadows 0\n            -interactiveBackFaceCull 0\n"
		+ "            -sortTransparent 1\n            -controllers 1\n            -nurbsCurves 1\n            -nurbsSurfaces 1\n            -polymeshes 1\n            -subdivSurfaces 1\n            -planes 1\n            -lights 1\n            -cameras 1\n            -controlVertices 1\n            -hulls 1\n            -grid 1\n            -imagePlane 1\n            -joints 1\n            -ikHandles 1\n            -deformers 1\n            -dynamics 1\n            -particleInstancers 1\n            -fluids 1\n            -hairSystems 1\n            -follicles 1\n            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n            -locators 1\n            -manipulators 1\n            -pluginShapes 1\n            -dimensions 1\n            -handles 1\n            -pivots 1\n            -textures 1\n            -strokes 1\n            -motionTrails 1\n            -clipGhosts 1\n            -greasePencils 1\n            -shadows 0\n            -captureSequenceNumber -1\n            -width 1\n            -height 1\n"
		+ "            -sceneRenderFilter 0\n            $editorName;\n        modelEditor -e -viewSelected 0 $editorName;\n        modelEditor -e \n            -pluginObjects \"gpuCacheDisplayFilter\" 1 \n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"modelPanel\" (localizedPanelLabel(\"Front View\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tmodelPanel -edit -l (localizedPanelLabel(\"Front View\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        modelEditor -e \n            -camera \"front\" \n            -useInteractiveMode 0\n            -displayLights \"default\" \n            -displayAppearance \"smoothShaded\" \n            -activeOnly 0\n            -ignorePanZoom 0\n            -wireframeOnShaded 0\n            -headsUpDisplay 1\n            -holdOuts 1\n            -selectionHiliteDisplay 1\n            -useDefaultMaterial 0\n            -bufferMode \"double\" \n            -twoSidedLighting 0\n            -backfaceCulling 0\n"
		+ "            -xray 0\n            -jointXray 0\n            -activeComponentsXray 0\n            -displayTextures 0\n            -smoothWireframe 0\n            -lineWidth 1\n            -textureAnisotropic 0\n            -textureHilight 1\n            -textureSampling 2\n            -textureDisplay \"modulate\" \n            -textureMaxSize 32768\n            -fogging 0\n            -fogSource \"fragment\" \n            -fogMode \"linear\" \n            -fogStart 0\n            -fogEnd 100\n            -fogDensity 0.1\n            -fogColor 0.5 0.5 0.5 1 \n            -depthOfFieldPreview 1\n            -maxConstantTransparency 1\n            -rendererName \"vp2Renderer\" \n            -objectFilterShowInHUD 1\n            -isFiltered 0\n            -colorResolution 256 256 \n            -bumpResolution 512 512 \n            -textureCompression 0\n            -transparencyAlgorithm \"frontAndBackCull\" \n            -transpInShadows 0\n            -cullingOverride \"none\" \n            -lowQualityLighting 0\n            -maximumNumHardwareLights 1\n            -occlusionCulling 0\n"
		+ "            -shadingModel 0\n            -useBaseRenderer 0\n            -useReducedRenderer 0\n            -smallObjectCulling 0\n            -smallObjectThreshold -1 \n            -interactiveDisableShadows 0\n            -interactiveBackFaceCull 0\n            -sortTransparent 1\n            -controllers 1\n            -nurbsCurves 1\n            -nurbsSurfaces 1\n            -polymeshes 1\n            -subdivSurfaces 1\n            -planes 1\n            -lights 1\n            -cameras 1\n            -controlVertices 1\n            -hulls 1\n            -grid 1\n            -imagePlane 1\n            -joints 1\n            -ikHandles 1\n            -deformers 1\n            -dynamics 1\n            -particleInstancers 1\n            -fluids 1\n            -hairSystems 1\n            -follicles 1\n            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n            -locators 1\n            -manipulators 1\n            -pluginShapes 1\n            -dimensions 1\n            -handles 1\n            -pivots 1\n"
		+ "            -textures 1\n            -strokes 1\n            -motionTrails 1\n            -clipGhosts 1\n            -greasePencils 1\n            -shadows 0\n            -captureSequenceNumber -1\n            -width 1\n            -height 1\n            -sceneRenderFilter 0\n            $editorName;\n        modelEditor -e -viewSelected 0 $editorName;\n        modelEditor -e \n            -pluginObjects \"gpuCacheDisplayFilter\" 1 \n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"modelPanel\" (localizedPanelLabel(\"Persp View\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tmodelPanel -edit -l (localizedPanelLabel(\"Persp View\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        modelEditor -e \n            -camera \"persp\" \n            -useInteractiveMode 0\n            -displayLights \"default\" \n            -displayAppearance \"smoothShaded\" \n            -activeOnly 0\n            -ignorePanZoom 0\n"
		+ "            -wireframeOnShaded 0\n            -headsUpDisplay 1\n            -holdOuts 1\n            -selectionHiliteDisplay 1\n            -useDefaultMaterial 0\n            -bufferMode \"double\" \n            -twoSidedLighting 0\n            -backfaceCulling 0\n            -xray 0\n            -jointXray 0\n            -activeComponentsXray 0\n            -displayTextures 1\n            -smoothWireframe 0\n            -lineWidth 1\n            -textureAnisotropic 0\n            -textureHilight 1\n            -textureSampling 2\n            -textureDisplay \"modulate\" \n            -textureMaxSize 32768\n            -fogging 0\n            -fogSource \"fragment\" \n            -fogMode \"linear\" \n            -fogStart 0\n            -fogEnd 100\n            -fogDensity 0.1\n            -fogColor 0.5 0.5 0.5 1 \n            -depthOfFieldPreview 1\n            -maxConstantTransparency 1\n            -rendererName \"base_OpenGL_Renderer\" \n            -objectFilterShowInHUD 1\n            -isFiltered 0\n            -colorResolution 256 256 \n            -bumpResolution 512 512 \n"
		+ "            -textureCompression 0\n            -transparencyAlgorithm \"frontAndBackCull\" \n            -transpInShadows 0\n            -cullingOverride \"none\" \n            -lowQualityLighting 0\n            -maximumNumHardwareLights 1\n            -occlusionCulling 0\n            -shadingModel 0\n            -useBaseRenderer 0\n            -useReducedRenderer 0\n            -smallObjectCulling 0\n            -smallObjectThreshold -1 \n            -interactiveDisableShadows 0\n            -interactiveBackFaceCull 0\n            -sortTransparent 1\n            -controllers 1\n            -nurbsCurves 1\n            -nurbsSurfaces 1\n            -polymeshes 1\n            -subdivSurfaces 1\n            -planes 1\n            -lights 1\n            -cameras 1\n            -controlVertices 1\n            -hulls 1\n            -grid 1\n            -imagePlane 1\n            -joints 1\n            -ikHandles 1\n            -deformers 1\n            -dynamics 1\n            -particleInstancers 1\n            -fluids 1\n            -hairSystems 1\n            -follicles 1\n"
		+ "            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n            -locators 1\n            -manipulators 1\n            -pluginShapes 1\n            -dimensions 1\n            -handles 1\n            -pivots 1\n            -textures 1\n            -strokes 1\n            -motionTrails 1\n            -clipGhosts 1\n            -greasePencils 1\n            -shadows 0\n            -captureSequenceNumber -1\n            -width 762\n            -height 847\n            -sceneRenderFilter 0\n            $editorName;\n        modelEditor -e -viewSelected 0 $editorName;\n        modelEditor -e \n            -pluginObjects \"gpuCacheDisplayFilter\" 1 \n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"outlinerPanel\" (localizedPanelLabel(\"ToggledOutliner\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\toutlinerPanel -edit -l (localizedPanelLabel(\"ToggledOutliner\")) -mbv $menusOkayInPanels  $panelName;\n"
		+ "\t\t$editorName = $panelName;\n        outlinerEditor -e \n            -showShapes 0\n            -showAssignedMaterials 0\n            -showTimeEditor 1\n            -showReferenceNodes 1\n            -showReferenceMembers 1\n            -showAttributes 0\n            -showConnected 0\n            -showAnimCurvesOnly 0\n            -showMuteInfo 0\n            -organizeByLayer 1\n            -organizeByClip 1\n            -showAnimLayerWeight 1\n            -autoExpandLayers 1\n            -autoExpand 0\n            -showDagOnly 1\n            -showAssets 1\n            -showContainedOnly 1\n            -showPublishedAsConnected 0\n            -showParentContainers 0\n            -showContainerContents 1\n            -ignoreDagHierarchy 0\n            -expandConnections 0\n            -showUpstreamCurves 1\n            -showUnitlessCurves 1\n            -showCompounds 1\n            -showLeafs 1\n            -showNumericAttrsOnly 0\n            -highlightActive 1\n            -autoSelectNewObjects 0\n            -doNotSelectNewObjects 0\n            -dropIsParent 1\n"
		+ "            -transmitFilters 0\n            -setFilter \"defaultSetFilter\" \n            -showSetMembers 1\n            -allowMultiSelection 1\n            -alwaysToggleSelect 0\n            -directSelect 0\n            -isSet 0\n            -isSetMember 0\n            -displayMode \"DAG\" \n            -expandObjects 0\n            -setsIgnoreFilters 1\n            -containersIgnoreFilters 0\n            -editAttrName 0\n            -showAttrValues 0\n            -highlightSecondary 0\n            -showUVAttrsOnly 0\n            -showTextureNodesOnly 0\n            -attrAlphaOrder \"default\" \n            -animLayerFilterOptions \"allAffecting\" \n            -sortOrder \"none\" \n            -longNames 0\n            -niceNames 1\n            -showNamespace 1\n            -showPinIcons 0\n            -mapMotionTrails 0\n            -ignoreHiddenAttribute 0\n            -ignoreOutlinerColor 0\n            -renderFilterVisible 0\n            -renderFilterIndex 0\n            -selectionOrder \"chronological\" \n            -expandAttribute 0\n            $editorName;\n"
		+ "\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"outlinerPanel\" (localizedPanelLabel(\"Outliner\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\toutlinerPanel -edit -l (localizedPanelLabel(\"Outliner\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        outlinerEditor -e \n            -showShapes 0\n            -showAssignedMaterials 0\n            -showTimeEditor 1\n            -showReferenceNodes 0\n            -showReferenceMembers 0\n            -showAttributes 0\n            -showConnected 0\n            -showAnimCurvesOnly 0\n            -showMuteInfo 0\n            -organizeByLayer 1\n            -organizeByClip 1\n            -showAnimLayerWeight 1\n            -autoExpandLayers 1\n            -autoExpand 0\n            -showDagOnly 1\n            -showAssets 1\n            -showContainedOnly 1\n            -showPublishedAsConnected 0\n            -showParentContainers 0\n            -showContainerContents 1\n            -ignoreDagHierarchy 0\n"
		+ "            -expandConnections 0\n            -showUpstreamCurves 1\n            -showUnitlessCurves 1\n            -showCompounds 1\n            -showLeafs 1\n            -showNumericAttrsOnly 0\n            -highlightActive 1\n            -autoSelectNewObjects 0\n            -doNotSelectNewObjects 0\n            -dropIsParent 1\n            -transmitFilters 0\n            -setFilter \"defaultSetFilter\" \n            -showSetMembers 1\n            -allowMultiSelection 1\n            -alwaysToggleSelect 0\n            -directSelect 0\n            -displayMode \"DAG\" \n            -expandObjects 0\n            -setsIgnoreFilters 1\n            -containersIgnoreFilters 0\n            -editAttrName 0\n            -showAttrValues 0\n            -highlightSecondary 0\n            -showUVAttrsOnly 0\n            -showTextureNodesOnly 0\n            -attrAlphaOrder \"default\" \n            -animLayerFilterOptions \"allAffecting\" \n            -sortOrder \"none\" \n            -longNames 0\n            -niceNames 1\n            -showNamespace 1\n            -showPinIcons 0\n"
		+ "            -mapMotionTrails 0\n            -ignoreHiddenAttribute 0\n            -ignoreOutlinerColor 0\n            -renderFilterVisible 0\n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"graphEditor\" (localizedPanelLabel(\"Graph Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Graph Editor\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = ($panelName+\"OutlineEd\");\n            outlinerEditor -e \n                -showShapes 1\n                -showAssignedMaterials 0\n                -showTimeEditor 1\n                -showReferenceNodes 0\n                -showReferenceMembers 0\n                -showAttributes 1\n                -showConnected 1\n                -showAnimCurvesOnly 1\n                -showMuteInfo 0\n                -organizeByLayer 1\n                -organizeByClip 1\n                -showAnimLayerWeight 1\n                -autoExpandLayers 1\n"
		+ "                -autoExpand 1\n                -showDagOnly 0\n                -showAssets 1\n                -showContainedOnly 0\n                -showPublishedAsConnected 0\n                -showParentContainers 1\n                -showContainerContents 0\n                -ignoreDagHierarchy 0\n                -expandConnections 1\n                -showUpstreamCurves 1\n                -showUnitlessCurves 1\n                -showCompounds 0\n                -showLeafs 1\n                -showNumericAttrsOnly 1\n                -highlightActive 0\n                -autoSelectNewObjects 1\n                -doNotSelectNewObjects 0\n                -dropIsParent 1\n                -transmitFilters 1\n                -setFilter \"0\" \n                -showSetMembers 0\n                -allowMultiSelection 1\n                -alwaysToggleSelect 0\n                -directSelect 0\n                -displayMode \"DAG\" \n                -expandObjects 0\n                -setsIgnoreFilters 1\n                -containersIgnoreFilters 0\n                -editAttrName 0\n"
		+ "                -showAttrValues 0\n                -highlightSecondary 0\n                -showUVAttrsOnly 0\n                -showTextureNodesOnly 0\n                -attrAlphaOrder \"default\" \n                -animLayerFilterOptions \"allAffecting\" \n                -sortOrder \"none\" \n                -longNames 0\n                -niceNames 1\n                -showNamespace 1\n                -showPinIcons 1\n                -mapMotionTrails 1\n                -ignoreHiddenAttribute 0\n                -ignoreOutlinerColor 0\n                -renderFilterVisible 0\n                $editorName;\n\n\t\t\t$editorName = ($panelName+\"GraphEd\");\n            animCurveEditor -e \n                -displayKeys 1\n                -displayTangents 0\n                -displayActiveKeys 0\n                -displayActiveKeyTangents 1\n                -displayInfinities 0\n                -displayValues 0\n                -autoFit 1\n                -autoFitTime 0\n                -snapTime \"integer\" \n                -snapValue \"none\" \n                -showResults \"off\" \n"
		+ "                -showBufferCurves \"off\" \n                -smoothness \"fine\" \n                -resultSamples 1\n                -resultScreenSamples 0\n                -resultUpdate \"delayed\" \n                -showUpstreamCurves 1\n                -showCurveNames 0\n                -showActiveCurveNames 0\n                -stackedCurves 0\n                -stackedCurvesMin -1\n                -stackedCurvesMax 1\n                -stackedCurvesSpace 0.2\n                -displayNormalized 0\n                -preSelectionHighlight 0\n                -constrainDrag 0\n                -classicMode 1\n                -valueLinesToggle 1\n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"dopeSheetPanel\" (localizedPanelLabel(\"Dope Sheet\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Dope Sheet\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = ($panelName+\"OutlineEd\");\n"
		+ "            outlinerEditor -e \n                -showShapes 1\n                -showAssignedMaterials 0\n                -showTimeEditor 1\n                -showReferenceNodes 0\n                -showReferenceMembers 0\n                -showAttributes 1\n                -showConnected 1\n                -showAnimCurvesOnly 1\n                -showMuteInfo 0\n                -organizeByLayer 1\n                -organizeByClip 1\n                -showAnimLayerWeight 1\n                -autoExpandLayers 1\n                -autoExpand 0\n                -showDagOnly 0\n                -showAssets 1\n                -showContainedOnly 0\n                -showPublishedAsConnected 0\n                -showParentContainers 1\n                -showContainerContents 0\n                -ignoreDagHierarchy 0\n                -expandConnections 1\n                -showUpstreamCurves 1\n                -showUnitlessCurves 0\n                -showCompounds 1\n                -showLeafs 1\n                -showNumericAttrsOnly 1\n                -highlightActive 0\n"
		+ "                -autoSelectNewObjects 0\n                -doNotSelectNewObjects 1\n                -dropIsParent 1\n                -transmitFilters 0\n                -setFilter \"0\" \n                -showSetMembers 0\n                -allowMultiSelection 1\n                -alwaysToggleSelect 0\n                -directSelect 0\n                -displayMode \"DAG\" \n                -expandObjects 0\n                -setsIgnoreFilters 1\n                -containersIgnoreFilters 0\n                -editAttrName 0\n                -showAttrValues 0\n                -highlightSecondary 0\n                -showUVAttrsOnly 0\n                -showTextureNodesOnly 0\n                -attrAlphaOrder \"default\" \n                -animLayerFilterOptions \"allAffecting\" \n                -sortOrder \"none\" \n                -longNames 0\n                -niceNames 1\n                -showNamespace 1\n                -showPinIcons 0\n                -mapMotionTrails 1\n                -ignoreHiddenAttribute 0\n                -ignoreOutlinerColor 0\n                -renderFilterVisible 0\n"
		+ "                $editorName;\n\n\t\t\t$editorName = ($panelName+\"DopeSheetEd\");\n            dopeSheetEditor -e \n                -displayKeys 1\n                -displayTangents 0\n                -displayActiveKeys 0\n                -displayActiveKeyTangents 0\n                -displayInfinities 0\n                -displayValues 0\n                -autoFit 0\n                -autoFitTime 0\n                -snapTime \"integer\" \n                -snapValue \"none\" \n                -outliner \"dopeSheetPanel1OutlineEd\" \n                -showSummary 1\n                -showScene 0\n                -hierarchyBelow 0\n                -showTicks 1\n                -selectionWindow 0 0 0 0 \n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"timeEditorPanel\" (localizedPanelLabel(\"Time Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Time Editor\")) -mbv $menusOkayInPanels  $panelName;\n"
		+ "\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"clipEditorPanel\" (localizedPanelLabel(\"Trax Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Trax Editor\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = clipEditorNameFromPanel($panelName);\n            clipEditor -e \n                -displayKeys 0\n                -displayTangents 0\n                -displayActiveKeys 0\n                -displayActiveKeyTangents 0\n                -displayInfinities 0\n                -displayValues 0\n                -autoFit 0\n                -autoFitTime 0\n                -snapTime \"none\" \n                -snapValue \"none\" \n                -initialized 0\n                -manageSequencer 0 \n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"sequenceEditorPanel\" (localizedPanelLabel(\"Camera Sequencer\")) `;\n"
		+ "\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Camera Sequencer\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = sequenceEditorNameFromPanel($panelName);\n            clipEditor -e \n                -displayKeys 0\n                -displayTangents 0\n                -displayActiveKeys 0\n                -displayActiveKeyTangents 0\n                -displayInfinities 0\n                -displayValues 0\n                -autoFit 0\n                -autoFitTime 0\n                -snapTime \"none\" \n                -snapValue \"none\" \n                -initialized 0\n                -manageSequencer 1 \n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"hyperGraphPanel\" (localizedPanelLabel(\"Hypergraph Hierarchy\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Hypergraph Hierarchy\")) -mbv $menusOkayInPanels  $panelName;\n"
		+ "\n\t\t\t$editorName = ($panelName+\"HyperGraphEd\");\n            hyperGraph -e \n                -graphLayoutStyle \"hierarchicalLayout\" \n                -orientation \"horiz\" \n                -mergeConnections 0\n                -zoom 1\n                -animateTransition 0\n                -showRelationships 1\n                -showShapes 0\n                -showDeformers 0\n                -showExpressions 0\n                -showConstraints 0\n                -showConnectionFromSelected 0\n                -showConnectionToSelected 0\n                -showConstraintLabels 0\n                -showUnderworld 0\n                -showInvisible 0\n                -transitionFrames 1\n                -opaqueContainers 0\n                -freeform 0\n                -imagePosition 0 0 \n                -imageScale 1\n                -imageEnabled 0\n                -graphType \"DAG\" \n                -heatMapDisplay 0\n                -updateSelection 1\n                -updateNodeAdded 1\n                -useDrawOverrideColor 0\n                -limitGraphTraversal -1\n"
		+ "                -range 0 0 \n                -iconSize \"smallIcons\" \n                -showCachedConnections 0\n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"hyperShadePanel\" (localizedPanelLabel(\"Hypershade\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Hypershade\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"visorPanel\" (localizedPanelLabel(\"Visor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Visor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"nodeEditorPanel\" (localizedPanelLabel(\"Node Editor\")) `;\n\tif ($nodeEditorPanelVisible || $nodeEditorWorkspaceControlOpen) {\n"
		+ "\t\tif (\"\" == $panelName) {\n\t\t\tif ($useSceneConfig) {\n\t\t\t\t$panelName = `scriptedPanel -unParent  -type \"nodeEditorPanel\" -l (localizedPanelLabel(\"Node Editor\")) -mbv $menusOkayInPanels `;\n\n\t\t\t$editorName = ($panelName+\"NodeEditorEd\");\n            nodeEditor -e \n                -allAttributes 0\n                -allNodes 0\n                -autoSizeNodes 1\n                -consistentNameSize 1\n                -createNodeCommand \"nodeEdCreateNodeCommand\" \n                -connectNodeOnCreation 0\n                -connectOnDrop 0\n                -copyConnectionsOnPaste 0\n                -connectionStyle \"bezier\" \n                -defaultPinnedState 0\n                -additiveGraphingMode 0\n                -settingsChangedCallback \"nodeEdSyncControls\" \n                -traversalDepthLimit -1\n                -keyPressCommand \"nodeEdKeyPressCommand\" \n                -nodeTitleMode \"name\" \n                -gridSnap 0\n                -gridVisibility 1\n                -crosshairOnEdgeDragging 0\n                -popupMenuScript \"nodeEdBuildPanelMenus\" \n"
		+ "                -showNamespace 1\n                -showShapes 1\n                -showSGShapes 0\n                -showTransforms 1\n                -useAssets 1\n                -syncedSelection 1\n                -extendToShapes 1\n                -editorMode \"default\" \n                -hasWatchpoint 0\n                $editorName;\n\t\t\t}\n\t\t} else {\n\t\t\t$label = `panel -q -label $panelName`;\n\t\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Node Editor\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = ($panelName+\"NodeEditorEd\");\n            nodeEditor -e \n                -allAttributes 0\n                -allNodes 0\n                -autoSizeNodes 1\n                -consistentNameSize 1\n                -createNodeCommand \"nodeEdCreateNodeCommand\" \n                -connectNodeOnCreation 0\n                -connectOnDrop 0\n                -copyConnectionsOnPaste 0\n                -connectionStyle \"bezier\" \n                -defaultPinnedState 0\n                -additiveGraphingMode 0\n                -settingsChangedCallback \"nodeEdSyncControls\" \n"
		+ "                -traversalDepthLimit -1\n                -keyPressCommand \"nodeEdKeyPressCommand\" \n                -nodeTitleMode \"name\" \n                -gridSnap 0\n                -gridVisibility 1\n                -crosshairOnEdgeDragging 0\n                -popupMenuScript \"nodeEdBuildPanelMenus\" \n                -showNamespace 1\n                -showShapes 1\n                -showSGShapes 0\n                -showTransforms 1\n                -useAssets 1\n                -syncedSelection 1\n                -extendToShapes 1\n                -editorMode \"default\" \n                -hasWatchpoint 0\n                $editorName;\n\t\t\tif (!$useSceneConfig) {\n\t\t\t\tpanel -e -l $label $panelName;\n\t\t\t}\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"createNodePanel\" (localizedPanelLabel(\"Create Node\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Create Node\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n"
		+ "\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"polyTexturePlacementPanel\" (localizedPanelLabel(\"UV Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"UV Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"renderWindowPanel\" (localizedPanelLabel(\"Render View\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Render View\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"shapePanel\" (localizedPanelLabel(\"Shape Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tshapePanel -edit -l (localizedPanelLabel(\"Shape Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n"
		+ "\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"posePanel\" (localizedPanelLabel(\"Pose Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tposePanel -edit -l (localizedPanelLabel(\"Pose Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"dynRelEdPanel\" (localizedPanelLabel(\"Dynamic Relationships\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Dynamic Relationships\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"relationshipPanel\" (localizedPanelLabel(\"Relationship Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Relationship Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n"
		+ "\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"referenceEditorPanel\" (localizedPanelLabel(\"Reference Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Reference Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"componentEditorPanel\" (localizedPanelLabel(\"Component Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Component Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"dynPaintScriptedPanelType\" (localizedPanelLabel(\"Paint Effects\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Paint Effects\")) -mbv $menusOkayInPanels  $panelName;\n"
		+ "\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"scriptEditorPanel\" (localizedPanelLabel(\"Script Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Script Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"profilerPanel\" (localizedPanelLabel(\"Profiler Tool\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Profiler Tool\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"contentBrowserPanel\" (localizedPanelLabel(\"Content Browser\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Content Browser\")) -mbv $menusOkayInPanels  $panelName;\n"
		+ "\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\tif ($useSceneConfig) {\n        string $configName = `getPanel -cwl (localizedPanelLabel(\"Current Layout\"))`;\n        if (\"\" != $configName) {\n\t\t\tpanelConfiguration -edit -label (localizedPanelLabel(\"Current Layout\")) \n\t\t\t\t-userCreated false\n\t\t\t\t-defaultImage \"\"\n\t\t\t\t-image \"\"\n\t\t\t\t-sc false\n\t\t\t\t-configString \"global string $gMainPane; paneLayout -e -cn \\\"single\\\" -ps 1 100 100 $gMainPane;\"\n\t\t\t\t-removeAllPanels\n\t\t\t\t-ap false\n\t\t\t\t\t(localizedPanelLabel(\"Persp View\")) \n\t\t\t\t\t\"modelPanel\"\n"
		+ "\t\t\t\t\t\"$panelName = `modelPanel -unParent -l (localizedPanelLabel(\\\"Persp View\\\")) -mbv $menusOkayInPanels `;\\n$editorName = $panelName;\\nmodelEditor -e \\n    -cam `findStartUpCamera persp` \\n    -useInteractiveMode 0\\n    -displayLights \\\"default\\\" \\n    -displayAppearance \\\"smoothShaded\\\" \\n    -activeOnly 0\\n    -ignorePanZoom 0\\n    -wireframeOnShaded 0\\n    -headsUpDisplay 1\\n    -holdOuts 1\\n    -selectionHiliteDisplay 1\\n    -useDefaultMaterial 0\\n    -bufferMode \\\"double\\\" \\n    -twoSidedLighting 0\\n    -backfaceCulling 0\\n    -xray 0\\n    -jointXray 0\\n    -activeComponentsXray 0\\n    -displayTextures 1\\n    -smoothWireframe 0\\n    -lineWidth 1\\n    -textureAnisotropic 0\\n    -textureHilight 1\\n    -textureSampling 2\\n    -textureDisplay \\\"modulate\\\" \\n    -textureMaxSize 32768\\n    -fogging 0\\n    -fogSource \\\"fragment\\\" \\n    -fogMode \\\"linear\\\" \\n    -fogStart 0\\n    -fogEnd 100\\n    -fogDensity 0.1\\n    -fogColor 0.5 0.5 0.5 1 \\n    -depthOfFieldPreview 1\\n    -maxConstantTransparency 1\\n    -rendererName \\\"base_OpenGL_Renderer\\\" \\n    -objectFilterShowInHUD 1\\n    -isFiltered 0\\n    -colorResolution 256 256 \\n    -bumpResolution 512 512 \\n    -textureCompression 0\\n    -transparencyAlgorithm \\\"frontAndBackCull\\\" \\n    -transpInShadows 0\\n    -cullingOverride \\\"none\\\" \\n    -lowQualityLighting 0\\n    -maximumNumHardwareLights 1\\n    -occlusionCulling 0\\n    -shadingModel 0\\n    -useBaseRenderer 0\\n    -useReducedRenderer 0\\n    -smallObjectCulling 0\\n    -smallObjectThreshold -1 \\n    -interactiveDisableShadows 0\\n    -interactiveBackFaceCull 0\\n    -sortTransparent 1\\n    -controllers 1\\n    -nurbsCurves 1\\n    -nurbsSurfaces 1\\n    -polymeshes 1\\n    -subdivSurfaces 1\\n    -planes 1\\n    -lights 1\\n    -cameras 1\\n    -controlVertices 1\\n    -hulls 1\\n    -grid 1\\n    -imagePlane 1\\n    -joints 1\\n    -ikHandles 1\\n    -deformers 1\\n    -dynamics 1\\n    -particleInstancers 1\\n    -fluids 1\\n    -hairSystems 1\\n    -follicles 1\\n    -nCloths 1\\n    -nParticles 1\\n    -nRigids 1\\n    -dynamicConstraints 1\\n    -locators 1\\n    -manipulators 1\\n    -pluginShapes 1\\n    -dimensions 1\\n    -handles 1\\n    -pivots 1\\n    -textures 1\\n    -strokes 1\\n    -motionTrails 1\\n    -clipGhosts 1\\n    -greasePencils 1\\n    -shadows 0\\n    -captureSequenceNumber -1\\n    -width 762\\n    -height 847\\n    -sceneRenderFilter 0\\n    $editorName;\\nmodelEditor -e -viewSelected 0 $editorName;\\nmodelEditor -e \\n    -pluginObjects \\\"gpuCacheDisplayFilter\\\" 1 \\n    $editorName\"\n"
		+ "\t\t\t\t\t\"modelPanel -edit -l (localizedPanelLabel(\\\"Persp View\\\")) -mbv $menusOkayInPanels  $panelName;\\n$editorName = $panelName;\\nmodelEditor -e \\n    -cam `findStartUpCamera persp` \\n    -useInteractiveMode 0\\n    -displayLights \\\"default\\\" \\n    -displayAppearance \\\"smoothShaded\\\" \\n    -activeOnly 0\\n    -ignorePanZoom 0\\n    -wireframeOnShaded 0\\n    -headsUpDisplay 1\\n    -holdOuts 1\\n    -selectionHiliteDisplay 1\\n    -useDefaultMaterial 0\\n    -bufferMode \\\"double\\\" \\n    -twoSidedLighting 0\\n    -backfaceCulling 0\\n    -xray 0\\n    -jointXray 0\\n    -activeComponentsXray 0\\n    -displayTextures 1\\n    -smoothWireframe 0\\n    -lineWidth 1\\n    -textureAnisotropic 0\\n    -textureHilight 1\\n    -textureSampling 2\\n    -textureDisplay \\\"modulate\\\" \\n    -textureMaxSize 32768\\n    -fogging 0\\n    -fogSource \\\"fragment\\\" \\n    -fogMode \\\"linear\\\" \\n    -fogStart 0\\n    -fogEnd 100\\n    -fogDensity 0.1\\n    -fogColor 0.5 0.5 0.5 1 \\n    -depthOfFieldPreview 1\\n    -maxConstantTransparency 1\\n    -rendererName \\\"base_OpenGL_Renderer\\\" \\n    -objectFilterShowInHUD 1\\n    -isFiltered 0\\n    -colorResolution 256 256 \\n    -bumpResolution 512 512 \\n    -textureCompression 0\\n    -transparencyAlgorithm \\\"frontAndBackCull\\\" \\n    -transpInShadows 0\\n    -cullingOverride \\\"none\\\" \\n    -lowQualityLighting 0\\n    -maximumNumHardwareLights 1\\n    -occlusionCulling 0\\n    -shadingModel 0\\n    -useBaseRenderer 0\\n    -useReducedRenderer 0\\n    -smallObjectCulling 0\\n    -smallObjectThreshold -1 \\n    -interactiveDisableShadows 0\\n    -interactiveBackFaceCull 0\\n    -sortTransparent 1\\n    -controllers 1\\n    -nurbsCurves 1\\n    -nurbsSurfaces 1\\n    -polymeshes 1\\n    -subdivSurfaces 1\\n    -planes 1\\n    -lights 1\\n    -cameras 1\\n    -controlVertices 1\\n    -hulls 1\\n    -grid 1\\n    -imagePlane 1\\n    -joints 1\\n    -ikHandles 1\\n    -deformers 1\\n    -dynamics 1\\n    -particleInstancers 1\\n    -fluids 1\\n    -hairSystems 1\\n    -follicles 1\\n    -nCloths 1\\n    -nParticles 1\\n    -nRigids 1\\n    -dynamicConstraints 1\\n    -locators 1\\n    -manipulators 1\\n    -pluginShapes 1\\n    -dimensions 1\\n    -handles 1\\n    -pivots 1\\n    -textures 1\\n    -strokes 1\\n    -motionTrails 1\\n    -clipGhosts 1\\n    -greasePencils 1\\n    -shadows 0\\n    -captureSequenceNumber -1\\n    -width 762\\n    -height 847\\n    -sceneRenderFilter 0\\n    $editorName;\\nmodelEditor -e -viewSelected 0 $editorName;\\nmodelEditor -e \\n    -pluginObjects \\\"gpuCacheDisplayFilter\\\" 1 \\n    $editorName\"\n"
		+ "\t\t\t\t$configName;\n\n            setNamedPanelLayout (localizedPanelLabel(\"Current Layout\"));\n        }\n\n        panelHistory -e -clear mainPanelHistory;\n        sceneUIReplacement -clear;\n\t}\n\n\ngrid -spacing 5 -size 12 -divisions 5 -displayAxes yes -displayGridLines yes -displayDivisionLines yes -displayPerspectiveLabels no -displayOrthographicLabels no -displayAxesBold yes -perspectiveLabelPosition axis -orthographicLabelPosition edge;\nviewManip -drawCompass 0 -compassAngle 0 -frontParameters \"\" -homeParameters \"\" -selectionLockParameters \"\";\n}\n");
	setAttr ".st" 3;
createNode script -n "sceneConfigurationScriptNode";
	rename -uid "5E6BAA2C-41D8-7661-7429-53A567C42563";
	setAttr ".b" -type "string" "playbackOptions -min 1 -max 120 -ast 1 -aet 200 ";
	setAttr ".st" 6;
select -ne :time1;
	setAttr ".o" 1;
	setAttr ".unw" 1;
select -ne :hardwareRenderingGlobals;
	setAttr ".otfna" -type "stringArray" 22 "NURBS Curves" "NURBS Surfaces" "Polygons" "Subdiv Surface" "Particles" "Particle Instance" "Fluids" "Strokes" "Image Planes" "UI" "Lights" "Cameras" "Locators" "Joints" "IK Handles" "Deformers" "Motion Trails" "Components" "Hair Systems" "Follicles" "Misc. UI" "Ornaments"  ;
	setAttr ".otfva" -type "Int32Array" 22 0 1 1 1 1 1
		 1 1 1 0 0 0 0 0 0 0 0 0
		 0 0 0 0 ;
	setAttr ".fprt" yes;
select -ne :renderPartition;
	setAttr -s 4 ".st";
select -ne :renderGlobalsList1;
select -ne :defaultShaderList1;
	setAttr -s 6 ".s";
select -ne :postProcessList1;
	setAttr -s 2 ".p";
select -ne :defaultRenderUtilityList1;
	setAttr -s 2 ".u";
select -ne :defaultRenderingList1;
select -ne :defaultTextureList1;
	setAttr -s 2 ".tx";
select -ne :initialShadingGroup;
	setAttr -s 2 ".dsm";
	setAttr ".ro" yes;
	setAttr -s 2 ".gn";
select -ne :initialParticleSE;
	setAttr ".ro" yes;
select -ne :defaultRenderGlobals;
	setAttr ".ren" -type "string" "arnold";
select -ne :defaultResolution;
	setAttr ".pa" 1;
select -ne :hardwareRenderGlobals;
	setAttr ".ctrs" 256;
	setAttr ".btrs" 512;
connectAttr "pasted__groupId28.id" "pasted__room1Shape.iog.og[0].gid";
connectAttr ":initialShadingGroup.mwc" "pasted__room1Shape.iog.og[0].gco";
connectAttr "pasted__groupId29.id" "pasted__room1Shape.iog.og[1].gid";
connectAttr "pasted__lambert2SG.mwc" "pasted__room1Shape.iog.og[1].gco";
connectAttr "pasted__groupId30.id" "pasted__room1Shape.iog.og[2].gid";
connectAttr "pasted__phong12SG.mwc" "pasted__room1Shape.iog.og[2].gco";
connectAttr "pasted__groupParts16.og" "pasted__roomShape.i";
connectAttr "pasted__groupId19.id" "pasted__roomShape.iog.og[0].gid";
connectAttr ":initialShadingGroup.mwc" "pasted__roomShape.iog.og[0].gco";
connectAttr "pasted__groupId21.id" "pasted__roomShape.iog.og[1].gid";
connectAttr "pasted__lambert2SG.mwc" "pasted__roomShape.iog.og[1].gco";
connectAttr "pasted__groupId27.id" "pasted__roomShape.iog.og[2].gid";
connectAttr "pasted__phong12SG.mwc" "pasted__roomShape.iog.og[2].gco";
connectAttr "pasted__polyTweakUV9.uvtk[0]" "pasted__roomShape.uvst[0].uvtw";
relationship "link" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "pasted__lambert2SG.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "pasted__phong12SG.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "pasted__lambert2SG.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "pasted__phong12SG.message" ":defaultLightSet.message";
connectAttr "layerManager.dli[0]" "defaultLayer.id";
connectAttr "renderLayerManager.rlmi[0]" "defaultRenderLayer.rlid";
connectAttr "pasted__lambert2.oc" "pasted__lambert2SG.ss";
connectAttr "pasted__groupId21.msg" "pasted__lambert2SG.gn" -na;
connectAttr "pasted__groupId29.msg" "pasted__lambert2SG.gn" -na;
connectAttr "pasted__roomShape.iog.og[1]" "pasted__lambert2SG.dsm" -na;
connectAttr "pasted__room1Shape.iog.og[1]" "pasted__lambert2SG.dsm" -na;
connectAttr "pasted__lambert2SG.msg" "pasted__materialInfo3.sg";
connectAttr "pasted__lambert2.msg" "pasted__materialInfo3.m";
connectAttr "pasted__file4.msg" "pasted__materialInfo3.t" -na;
connectAttr "pasted__file4.oc" "pasted__lambert2.c";
connectAttr ":defaultColorMgtGlobals.cme" "pasted__file4.cme";
connectAttr ":defaultColorMgtGlobals.cfe" "pasted__file4.cmcf";
connectAttr ":defaultColorMgtGlobals.cfp" "pasted__file4.cmcp";
connectAttr ":defaultColorMgtGlobals.wsn" "pasted__file4.ws";
connectAttr "pasted__place2dTexture4.c" "pasted__file4.c";
connectAttr "pasted__place2dTexture4.tf" "pasted__file4.tf";
connectAttr "pasted__place2dTexture4.rf" "pasted__file4.rf";
connectAttr "pasted__place2dTexture4.mu" "pasted__file4.mu";
connectAttr "pasted__place2dTexture4.mv" "pasted__file4.mv";
connectAttr "pasted__place2dTexture4.s" "pasted__file4.s";
connectAttr "pasted__place2dTexture4.wu" "pasted__file4.wu";
connectAttr "pasted__place2dTexture4.wv" "pasted__file4.wv";
connectAttr "pasted__place2dTexture4.re" "pasted__file4.re";
connectAttr "pasted__place2dTexture4.of" "pasted__file4.of";
connectAttr "pasted__place2dTexture4.r" "pasted__file4.ro";
connectAttr "pasted__place2dTexture4.n" "pasted__file4.n";
connectAttr "pasted__place2dTexture4.vt1" "pasted__file4.vt1";
connectAttr "pasted__place2dTexture4.vt2" "pasted__file4.vt2";
connectAttr "pasted__place2dTexture4.vt3" "pasted__file4.vt3";
connectAttr "pasted__place2dTexture4.vc1" "pasted__file4.vc1";
connectAttr "pasted__place2dTexture4.o" "pasted__file4.uv";
connectAttr "pasted__place2dTexture4.ofs" "pasted__file4.fs";
connectAttr "pasted__phong12.oc" "pasted__phong12SG.ss";
connectAttr "pasted__groupId27.msg" "pasted__phong12SG.gn" -na;
connectAttr "pasted__groupId30.msg" "pasted__phong12SG.gn" -na;
connectAttr "pasted__roomShape.iog.og[2]" "pasted__phong12SG.dsm" -na;
connectAttr "pasted__room1Shape.iog.og[2]" "pasted__phong12SG.dsm" -na;
connectAttr "pasted__phong12SG.msg" "pasted__materialInfo13.sg";
connectAttr "pasted__phong12.msg" "pasted__materialInfo13.m";
connectAttr "pasted__file13.msg" "pasted__materialInfo13.t" -na;
connectAttr "pasted__file13.oc" "pasted__phong12.c";
connectAttr ":defaultColorMgtGlobals.cme" "pasted__file13.cme";
connectAttr ":defaultColorMgtGlobals.cfe" "pasted__file13.cmcf";
connectAttr ":defaultColorMgtGlobals.cfp" "pasted__file13.cmcp";
connectAttr ":defaultColorMgtGlobals.wsn" "pasted__file13.ws";
connectAttr "pasted__place2dTexture13.c" "pasted__file13.c";
connectAttr "pasted__place2dTexture13.tf" "pasted__file13.tf";
connectAttr "pasted__place2dTexture13.rf" "pasted__file13.rf";
connectAttr "pasted__place2dTexture13.mu" "pasted__file13.mu";
connectAttr "pasted__place2dTexture13.mv" "pasted__file13.mv";
connectAttr "pasted__place2dTexture13.s" "pasted__file13.s";
connectAttr "pasted__place2dTexture13.wu" "pasted__file13.wu";
connectAttr "pasted__place2dTexture13.wv" "pasted__file13.wv";
connectAttr "pasted__place2dTexture13.re" "pasted__file13.re";
connectAttr "pasted__place2dTexture13.of" "pasted__file13.of";
connectAttr "pasted__place2dTexture13.r" "pasted__file13.ro";
connectAttr "pasted__place2dTexture13.n" "pasted__file13.n";
connectAttr "pasted__place2dTexture13.vt1" "pasted__file13.vt1";
connectAttr "pasted__place2dTexture13.vt2" "pasted__file13.vt2";
connectAttr "pasted__place2dTexture13.vt3" "pasted__file13.vt3";
connectAttr "pasted__place2dTexture13.vc1" "pasted__file13.vc1";
connectAttr "pasted__place2dTexture13.o" "pasted__file13.uv";
connectAttr "pasted__place2dTexture13.ofs" "pasted__file13.fs";
connectAttr "pasted__polyTweakUV9.out" "pasted__groupParts16.ig";
connectAttr "pasted__groupId27.id" "pasted__groupParts16.gi";
connectAttr "pasted__groupParts12.og" "pasted__polyTweakUV9.ip";
connectAttr "pasted__polyAutoProj6.out" "pasted__groupParts12.ig";
connectAttr "pasted__groupId21.id" "pasted__groupParts12.gi";
connectAttr "pasted__groupParts9.og" "pasted__polyAutoProj6.ip";
connectAttr "pasted__roomShape.wm" "pasted__polyAutoProj6.mp";
connectAttr "|ROOM|pasted__room|pasted__polySurfaceShape5.o" "pasted__groupParts9.ig"
		;
connectAttr "pasted__groupId19.id" "pasted__groupParts9.gi";
connectAttr "pasted__lambert2SG.pa" ":renderPartition.st" -na;
connectAttr "pasted__phong12SG.pa" ":renderPartition.st" -na;
connectAttr "pasted__lambert2.msg" ":defaultShaderList1.s" -na;
connectAttr "pasted__phong12.msg" ":defaultShaderList1.s" -na;
connectAttr "pasted__place2dTexture4.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "pasted__place2dTexture13.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "defaultRenderLayer.msg" ":defaultRenderingList1.r" -na;
connectAttr "pasted__file4.msg" ":defaultTextureList1.tx" -na;
connectAttr "pasted__file13.msg" ":defaultTextureList1.tx" -na;
connectAttr "pasted__roomShape.iog.og[0]" ":initialShadingGroup.dsm" -na;
connectAttr "pasted__room1Shape.iog.og[0]" ":initialShadingGroup.dsm" -na;
connectAttr "pasted__groupId19.msg" ":initialShadingGroup.gn" -na;
connectAttr "pasted__groupId28.msg" ":initialShadingGroup.gn" -na;
// End of room.ma
