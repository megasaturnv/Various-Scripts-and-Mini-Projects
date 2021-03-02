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
module circuitBoardMountingPosts(width=100, length=50, screwHoleHeight=5, screwHoleOuterDiameter=6, screwHoleInnerDiameter=3) {
	for (i=[-1,1], j=[-1,1]) {
		translate([i*(width/2), j*(length/2), 0]) difference() {
			cylinder(d=screwHoleOuterDiameter, h=screwHoleHeight);
			cylinder(d=screwHoleInnerDiameter, h=screwHoleHeight+0.01);
		}
	}
}

module dovetailJoint(a=6, b=12, h=5, thickness=2, center=true) {
	if (center)	{
		translate([-b/2, 0, 0])
		linear_extrude (height=thickness)
		polygon(points=[[0,0],[b,0],[a/2+b/2,h],[b/2-a/2,h]]);
	} else {
		linear_extrude (height=thickness)
		polygon(points=[[0,0],[b,0],[a/2+b/2,h],[b/2-a/2,h]]);
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
translate([0, 60, 0]) circuitBoardMountingPosts();

translate([10, 0, 0]) difference() {
	union() {
		cube([30,30,2]);
		translate([15, -3, 0]) dovetailJoint(4, 8, 3, 2, true);
		translate([15, 15, 2]) circuitBoardMountingPosts(15, 15, 3, 6, 3);
	}

	translate([15, 27, -0.01]) dovetailJoint(4, 8, 3, 2.02, true);

	translate([0,  0,  -0.01]) rotate([0, 0, 0])   roundedCorner(4, 2.02, false);
	translate([30, 0,  -0.01]) rotate([0, 0, 90])  roundedCorner(4, 2.02, false);
	translate([30, 30, -0.01]) rotate([0, 0, 180]) roundedCorner(4, 2.02, false);
	translate([0,  30, -0.01]) rotate([0, 0, 270]) roundedCorner(4, 2.02, false);

	translate([15, 15, 1.01]) drawAvatar(1.5, 1, true);
}
