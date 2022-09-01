// by MegaSaturnv

/////////////////////////////
// Customizable Parameters //
/////////////////////////////
/* [Basic] */

/* [Advanced] */
//Use $fn = 24 if it's a preview. $fn = 96 for the render. Increase 96 to produce a smoother curve.
$fn = $preview ? 24 : 96;

/////////////
// Modules //
/////////////
module screwMountingPosts(width=50, length=30, screwHoleHeight=5, screwHoleOuterDiameter=6, screwHoleInnerDiameter=3, screwHoleInnerDepth=3, center=true, justHole=false) {
	if (center) {
		for (i=[-1,1], j=[-1,1]) {
			translate([i*(width/2), j*(length/2), 0]) difference() {
				if (!justHole) cylinder(d=screwHoleOuterDiameter, h=screwHoleHeight);
				translate([0,0,screwHoleHeight-screwHoleInnerDepth]) cylinder(d=screwHoleInnerDiameter, h=screwHoleInnerDepth+0.01);
			}
		}
	} else {
		for (i=[0,2], j=[0,2]) {
			translate([i*(width/2), j*(length/2), 0]) difference() {
				if (!justHole) cylinder(d=screwHoleOuterDiameter, h=screwHoleHeight);
				translate([0,0,screwHoleHeight-screwHoleInnerDepth]) cylinder(d=screwHoleInnerDiameter, h=screwHoleInnerDepth+0.01);
			}
		}
	}
}

module dovetailJoint(a=7.5, b=15, h=5, thickness=2, center=true, centeredAround="b", tolerance=0.3, gender="male") {
	at = a - tolerance;
	bt = b - tolerance;
	ht = h + tolerance;

	if (center)	{
		if (centeredAround=="a") {
			if (gender == "male") {
				translate([-bt/2, -h, 0])
				linear_extrude(height=thickness)
				polygon(points=[[0,0],[bt,0],[at/2+bt/2,h],[bt/2-at/2,h]]);
			} else if (gender == "female") {
				translate([-b/2, -ht + 0.0001, 0])
				linear_extrude(height=thickness)
				polygon(points=[[0,0],[b,0],[a/2+b/2,ht],[b/2-a/2,ht]]);
			}
		} else if (centeredAround=="b") {
			if (gender == "male") {
				translate([-bt/2, 0, 0])
				linear_extrude(height=thickness)
				polygon(points=[[0,0],[bt,0],[at/2+bt/2,h],[bt/2-at/2,h]]);
			} else if (gender == "female") {
				translate([-b/2, 0, 0])
				linear_extrude(height=thickness)
				polygon(points=[[0,0],[b,0],[a/2+b/2,ht],[b/2-a/2,ht]]);
			}
		}
	} else {
		if (centeredAround=="a") {
			if (gender == "male") {
				translate([0, -h, 0])
				linear_extrude(height=thickness)
				polygon(points=[[0,0],[bt,0],[at/2+bt/2,h],[bt/2-at/2,h]]);
			} else if (gender == "female") {
				translate([0, -ht, 0])
				linear_extrude(height=thickness)
				polygon(points=[[0,0],[b,0],[a/2+b/2,ht],[b/2-a/2,ht]]);
			}
		} else if (centeredAround=="b") {
			if (gender == "male") {
				linear_extrude(height=thickness)
				polygon(points=[[0,0],[bt,0],[at/2+bt/2,h],[bt/2-at/2,h]]);
			} else if (gender == "female") {
				linear_extrude(height=thickness)
				polygon(points=[[0,0],[b,0],[a/2+b/2,ht],[b/2-a/2,ht]]);
			}
		}
	}
}

module drawAvatar(pxSize=2, thickness=2, center=true) {
    avatar = [
    " X X ",
    "XX XX",
    " XXX ",
    "  X  ",
    "X X X"];
    for (i = [0 : len(avatar)-1], j = [0 : len(avatar[i])-1]) {
        if (avatar[i][j] == "X") {
			if (center)	{
				translate([-(len(avatar)*pxSize)/2, -(len(avatar[0])*pxSize)/2, 0])
				translate([i*pxSize, j*pxSize, 0])
				cube([pxSize, pxSize, thickness]);
			} else {
				translate([i*pxSize, j*pxSize, 0])
				cube([pxSize, pxSize, thickness]);
			}
        }
    }
}

module roundedCorner(sideLength=8, thickness=2, cylinderCenter=false) {
	difference() {
		cube([sideLength, sideLength, thickness]);
		if (cylinderCenter) { //Cylinder cutout is in the centre
			translate([0, 0, -0.01]) cylinder(r=sideLength, h=thickness+0.02);
		} else { //Corner of the object is in the centre
			translate([sideLength, sideLength, -0.01]) cylinder(r=sideLength, h=thickness+0.02);
		}
	}
}

module triangle(XLength=5, YLength=8, thickness=2) {
    linear_extrude(height=thickness)
    {
        polygon(points=[[0,0],[XLength,0],[0,YLength]], paths=[[0,1,2]]);
    }
}

////////////////
// Main Model //
////////////////
translate([0, 0, 0])  color("lightgreen") drawAvatar();
translate([0, 10, 0]) dovetailJoint();
translate([0, 20, 0]) roundedCorner();
translate([0, 30, 0]) triangle();
translate([0, 60, 0]) screwMountingPosts();
//dovetailJoint(a=7.5, b=15, h=5, thickness=2, center=true, centeredAround="b", tolerance=0.3, gender="male")
translate([10, 0, 0]) difference() {
	union() {
		cube([30,30,2]);
		translate([15, -3, 0]) dovetailJoint(4, 8, 3, 2, true, gender="male");
		translate([15, 15, 2]) screwMountingPosts(15, 15, 3, 6, 3);
	}

	translate([15, 27, -0.01]) dovetailJoint(4, 8, 3, 2.02, true, gender="female");

	translate([0,  0,  -0.01]) rotate([0, 0, 0])   roundedCorner(4, 2.02, false);
	translate([30, 0,  -0.01]) rotate([0, 0, 90])  roundedCorner(4, 2.02, false);
	translate([30, 30, -0.01]) rotate([0, 0, 180]) roundedCorner(4, 2.02, false);
	translate([0,  30, -0.01]) rotate([0, 0, 270]) roundedCorner(4, 2.02, false);

	translate([15, 15, 1.01]) drawAvatar(1.5, 1, true);
}
