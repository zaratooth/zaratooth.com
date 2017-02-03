import maya.cmds as cmds
import random
import math

#cmds.file(f=True, new=True)
cmds.namespace(set=":")

window = cmds.window(title="Lego Blocks", menuBar=True, widthHeight=(483, 500))

cmds.columnLayout()
#BASIC BLOCK SECTION
cmds.frameLayout('Blocks', collapsable=True, width=475)
cmds.tabLayout()
cmds.columnLayout('Square Block', width=475)
cmds.intSliderGrp('blockHeight', label="Height", field=True, min=1, max=20, value=3)
cmds.intSliderGrp('blockWidth', label="Width", field=True, min=1, max=20, value=2)
cmds.intSliderGrp('blockDepth', label="Depth", field=True, min=1, max=20, value=8)
cmds.colorSliderGrp('basicBlockColour', label="Colour", hsv=(120,1,1))
cmds.columnLayout()
cmds.button(label="Create Square Block", command=('basicBlock()'))
cmds.setParent('..')
cmds.setParent('..')

#SQUARE BLOCKS WITH HOLES
cmds.columnLayout("Square Block (Holes)", width=475)
cmds.intSliderGrp('squareHolesWidth', label="Width (# of nubs on Top)", field=True, min=2, max=8, value=4)
cmds.colorSliderGrp('squareBlocksColour', label="Colour", hsv=(10,1,1))
cmds.columnLayout()
cmds.button(label="Create Square Block with Holes", command=('squareBlocksWithHoles()'))
cmds.setParent('..')
cmds.setParent('..')

#ROUNDED BLOCKS WITH HOLES
cmds.columnLayout('Rounded Block (Holes)', width=475)
cmds.intSliderGrp('roundedHolesWidth', label="Width (# of inner holes)", field=True, min=2, max=15, value=3)
cmds.colorSliderGrp('roundedBlocksColour', label="Colour", hsv=(10,1,1))
cmds.radioButtonGrp('endPieces', nrb=4, labelArray4=["Left end", "Right end", "Both end", "None"], sl=4)
cmds.columnLayout()
cmds.button(label="Create Rounded Block with Holes", command=('roundedBlocksWithHoles()'))
cmds.setParent('..')
cmds.setParent('..')

#ROUNDED WITH HOLES AT ANGLE
cmds.columnLayout('Rounded Block (Angle)', width=475)
cmds.intSliderGrp('angleWidth', label="Length (# of holes across)", field=True, min=3, max=6, value=4)
cmds.intSliderGrp('angleHeight', label="Height (# of holes high)", field=True, min=2, max=4, value=2)
cmds.colorSliderGrp('angleBlocksColour', label="Colour", hsv=(10,1,1))
cmds.radioButtonGrp('angleEndPieces', nrb=4, labelArray4=["Left end", "Right end", "Both end", "None"], sl=4)
cmds.columnLayout()
cmds.rowLayout(nc=3)
cmds.button(label="Bends at 90 degrees", command=('roundedBlocksAtAngle(90, False)'))
cmds.button(label="Bends at 53 degrees", command=('roundedBlocksAtAngle(53.31, False)'))
cmds.button(label="Double Angle Beam", command=('roundedBlocksAtAngle(45, True)'))
cmds.setParent('..')
cmds.setParent('..')
cmds.setParent('..')
#tab and column layout end
cmds.setParent('..')
cmds.setParent('..')

#SPECIAL PIECES
cmds.frameLayout(label="Wheels",  collapsable=True, width=475)
cmds.columnLayout()
cmds.button(label="Create Wheel and Hub", command=('WheelAndHub()'))
cmds.setParent('..')
cmds.setParent('..')

cmds.frameLayout(label="Axels",  collapsable=True, width=475)
cmds.columnLayout()
cmds.intSliderGrp('axelLength', label="Length", field=True, min=2, max=12, value=4)
cmds.checkBox('stopper', label='Add a stopper to end')
cmds.radioButtonGrp('axelColor', nrb=2, labelArray2=["Grey", "Black"], sl=1)
cmds.button(label="Create Axel", command=('Axel()'))
cmds.setParent('..')
cmds.setParent('..')

cmds.frameLayout(label='Connectors and Spacers',  collapsable=True, width=475)
cmds.columnLayout()
cmds.gridLayout(nc=3, cw=475/3)
cmds.checkBox('blackConnecter', label='Black Connecter')
cmds.checkBox('blueConnecter', label='Blue Connecter')
cmds.checkBox('blackDoubleConnecter', label='Double Black Connecter')
cmds.checkBox('blackSpacerConnecter', label='Black Connecter with Spacer')
cmds.checkBox('greySpacer', label='Grey Spacer')
cmds.checkBox('greyDoubleSpacer', label='Double Grey Spacer')
cmds.checkBox('axelDoubleSpacer', label='Axel and Double Spacer')
cmds.checkBox('redAxelConnector', label='Red Axel Connector')
cmds.checkBox('longBallConnector', label='Long Ball Connector')
cmds.checkBox('greyHalfConnector', label='Grey Half Connector')
cmds.checkBox('ballAxelConnector', label='Ball and Axel Connector')
cmds.checkBox('DoubleSpacerHole', label='Double Spacer and Hole')
cmds.button(label="Create Connecters", command=('Connectors()'))
cmds.setParent('..')
cmds.setParent('..')

#wrapper col layout end
cmds.setParent('..')
#Show window
cmds.showWindow(window)

#square blocks with holes function
def squareBlocksWithHoles():
    
    #get width and color from ui 
    squareholesWidth = cmds.intSliderGrp('squareHolesWidth', query=True, value=True)
    rgb = cmds.colorSliderGrp('squareBlocksColour', query=True, rgbValue=True)
    
    #proper measurements
    cubeX = squareholesWidth * 0.8
    cubeY = 0.96
    cubeZ = 0.8
    
    rnd = random.randrange(0,1000)
    namespace_tmp = "squareHoles_"+str(rnd)
    cmds.select(clear=True)
    cmds.namespace(add=namespace_tmp)
    cmds.namespace(set=namespace_tmp)
    
    #create base block
    cube = cmds.polyCube(h=cubeY, w=cubeX, d=cubeZ, sx=squareholesWidth, name='baseBlock')
    print cube[0]
   
    #add middle cylinders
    j=0
    while j < (squareholesWidth -1):
        littleCyl = cmds.polyCylinder(r=0.25, h=cubeZ)
        bigCyl1 = cmds.polyCylinder(r=0.32, h=0.09)
        cmds.move((cubeZ/2), moveY=True, a=True)
        littleCyl = cmds.polyBoolOp(bigCyl1[0], littleCyl[0], ch=False, op=1)
        
        bigCyl2 = cmds.polyCylinder(r=0.32, h=0.09)
        cmds.move((-cubeZ/2), moveY=True, a=True)
        littleCyl = cmds.polyBoolOp(bigCyl2[0], littleCyl[0], ch=False, op=1)
        
        cmds.move(0.1, moveY=True, a=True)
        cmds.move(( (j*0.8) - (cubeX/2.0) + 0.8), moveX=True, a=True)
        cmds.rotate(90, rotateX=True, a=True)
        cube = cmds.polyBoolOp(cube[0], littleCyl[0], ch=False, op=2)
        j = j+1
    
    #add top cylinders
    for i in range(squareholesWidth):
        bigCyl = cmds.polyCylinder(r=0.25, h=0.2)
        littleCyl = cmds.polyCylinder(r=0.15, h=0.2)
        bigCyl = cmds.polyBoolOp(bigCyl[0], littleCyl[0], ch=False, op=2)
        cmds.move((cubeY/2.0 + 0.1), moveY=True, a=True)
        cmds.move(( (i*0.8) - (cubeX/2.0) + 0.4), moveX=True, a=True)
    
    myShader = cmds.shadingNode('lambert', asShader=True, name="blockMaterial")
    
    cmds.setAttr(namespace_tmp+":blockMaterial.color", rgb[0], rgb[1], rgb[2], type='double3')
    cmds.polyUnite((namespace_tmp+":*"), n=namespace_tmp, ch=False)
    cmds.delete(ch=True)
    
    cmds.hyperShade(assign=(namespace_tmp+":blockMaterial"))
    cmds.namespace(set=":")

#round blocks with holes
def roundedBlocksWithHoles():
   #get width and color from ui 
    roundholesWidth = cmds.intSliderGrp('roundedHolesWidth', query=True, value=True)
    axelHole = cmds.radioButtonGrp('endPieces', query=True, sl=True)
    rgb = cmds.colorSliderGrp('roundedBlocksColour', query=True, rgbValue=True)
    
    #proper measurements
    cubeX = (roundholesWidth-1) * 0.8
    cubeY = 0.76
    cubeZ = 0.8
    axelHeight = 0.5
    axelWidth = axelHeight/3
    axelDepth = 0.8
    
    rnd = random.randrange(0,1000)
    namespace_tmp = "roundedHoles_"+str(rnd)
    cmds.select(clear=True)
    cmds.namespace(add=namespace_tmp)
    cmds.namespace(set=namespace_tmp)
    
    #create base block
    roundedBlock = cmds.polyCube(h=cubeY, w=cubeX, d=cubeZ, sx=roundholesWidth-1, name='baseBlock')
   
    cylinder1 =  cmds.polyCylinder(r=0.38, h=cubeZ)
    cmds.move((-cubeX/2), moveX=True, a=True)
    cmds.rotate(90, rotateX=True, a=True)
    roundedBlock = cmds.polyBoolOp(roundedBlock[0], cylinder1[0], ch=False, op=1)
    
    cylinder2 =  cmds.polyCylinder(r=0.38, h=cubeZ)
    cmds.move((cubeX/2), moveX=True, a=True)
    cmds.rotate(90, rotateX=True, a=True)
    roundedBlock = cmds.polyBoolOp(roundedBlock[0], cylinder2[0], ch=False, op=1)
       
    #add middle cylinders
    j=0
    while j < roundholesWidth:
        endNum = roundholesWidth-1
        
        if ( axelHole==1 and j==0 ) or ( axelHole==2 and j==endNum ) or ( axelHole==3 and (j==0 or j==endNum) ):                       
            cyl = cmds.polyCylinder(r=0.25, h=axelDepth)
            cmds.rotate(90, rotateX=True, a=True)
            
            veticalRect = cmds.polyCube(h=axelHeight, w=axelWidth, d=axelDepth)
            horizonalRect = cmds.polyCube(h=axelHeight, w=axelWidth, d=axelDepth)
            cmds.rotate(90, rotateZ=True, a=True)            
            axel = cmds.polyBoolOp(veticalRect[0], horizonalRect[0], ch=False, op=1)   
            axel = cmds.polyBoolOp(axel[0], cyl[0], ch=False, op=3)    
            cmds.move(( (j*0.8) - (cubeX/2.0)), moveX=True, a=True)
            roundedBlock = cmds.polyBoolOp(roundedBlock[0], axel[0], ch=False, op=2)    
        else:
            littleCyl = cmds.polyCylinder(r=0.25, h=cubeZ)
            bigCyl1 = cmds.polyCylinder(r=0.32, h=0.09)
            cmds.move((cubeZ/2), moveY=True, a=True)
            littleCyl = cmds.polyBoolOp(bigCyl1[0], littleCyl[0], ch=False, op=1)
            
            bigCyl2 = cmds.polyCylinder(r=0.32, h=0.09)
            cmds.move((-cubeZ/2), moveY=True, a=True)
            finalCyl = cmds.polyBoolOp(bigCyl2[0], littleCyl[0], ch=False, op=1)                     
            cmds.move(( (j*0.8) - (cubeX/2.0)), moveX=True, a=True)
            cmds.rotate(90, rotateX=True, a=True)
            roundedBlock = cmds.polyBoolOp(roundedBlock[0], finalCyl[0], ch=False, op=2)
        j = j+1
    
    myShader = cmds.shadingNode('lambert', asShader=True, name="blockMaterial")
    
    cmds.setAttr(namespace_tmp+":blockMaterial.color", rgb[0], rgb[1], rgb[2], type='double3')
    cmds.select(namespace_tmp+":*")
    cmds.delete(ch=True)
    
    cmds.hyperShade(assign=(namespace_tmp+":blockMaterial"))
    cmds.namespace(set=":")
    
#rounded blocks at an angle
def roundedBlocksAtAngle( angle, extraBend ):
    #get width and color from ui 
    rowLength = cmds.intSliderGrp('angleWidth', query=True, value=True)
    rowHeight = cmds.intSliderGrp('angleHeight', query=True, value=True)
    axelHole = cmds.radioButtonGrp('angleEndPieces', query=True, sl=True)
    rgb = cmds.colorSliderGrp('angleBlocksColour', query=True, rgbValue=True)
    
    rnd = random.randrange(0,1000)
    namespace_tmp = "roundedHoles_"+str(rnd)
    cmds.select(clear=True)
    cmds.namespace(add=namespace_tmp)
    cmds.namespace(set=namespace_tmp)
    
    dimensions = dict(length=rowLength, height=rowHeight)
    
    for dimension, numHoles in dimensions.iteritems():      
        axelHeight = 0.5
        axelWidth = axelHeight/3
        axelDepth = 0.8
    
        cubeX = (numHoles-1) * 0.8
        cubeY = 0.76
        cubeZ = 0.8
        #create base block
        subdivisons = (numHoles-1)*2
        roundedBlock = cmds.polyCube(h=cubeY, w=cubeX, d=cubeZ, sx=subdivisons)
       
        cylinder1 =  cmds.polyCylinder(r=0.38, h=cubeZ)
        cmds.move((cubeX/2), moveX=True, a=True)
        cmds.rotate(90, rotateX=True, a=True)
        roundedBlock = cmds.polyBoolOp(roundedBlock[0], cylinder1[0], ch=False, op=1)
        
        cylinder2 =  cmds.polyCylinder(r=0.38, h=cubeZ)
        cmds.move((-cubeX/2), moveX=True, a=True)
        cmds.rotate(90, rotateX=True, a=True)
        roundedBlock = cmds.polyBoolOp(roundedBlock[0], cylinder2[0], ch=False, op=1)
       
        #add middle cylinders
        j=0
        endpiece=numHoles-1
        while j < numHoles:
            if ( axelHole==1 and j==0 and dimension=='length') or ( axelHole==2 and j==endpiece and dimension=='height') or ( axelHole==3 and ( (j==0 and dimension=='length') or (j==endpiece and dimension=='height') ) ):                       
                cyl = cmds.polyCylinder(r=0.25, h=axelDepth)
                cmds.rotate(90, rotateX=True, a=True)
                
                veticalRect = cmds.polyCube(h=axelHeight, w=axelWidth, d=axelDepth)
                horizonalRect = cmds.polyCube(h=axelHeight, w=axelWidth, d=axelDepth)
                cmds.rotate(90, rotateZ=True, a=True)            
                axel = cmds.polyBoolOp(veticalRect[0], horizonalRect[0], ch=False, op=1)   
                axel = cmds.polyBoolOp(axel[0], cyl[0], ch=False, op=3)    
                cmds.move(( (j*0.8) - (cubeX/2.0)), moveX=True, a=True)
                roundedBlock = cmds.polyBoolOp(roundedBlock[0], axel[0], ch=False, op=2)          
            else:
                littleCyl = cmds.polyCylinder(r=0.25, h=cubeZ)
                bigCyl1 = cmds.polyCylinder(r=0.32, h=0.09)
                cmds.move((cubeZ/2), moveY=True, a=True)
                littleCyl = cmds.polyBoolOp(bigCyl1[0], littleCyl[0], ch=False, op=1)
                
                bigCyl2 = cmds.polyCylinder(r=0.32, h=0.09)
                cmds.move((-cubeZ/2), moveY=True, a=True)
                finalCyl = cmds.polyBoolOp(bigCyl2[0], littleCyl[0], ch=False, op=1)                     
                cmds.move(( (j*0.8) - (cubeX/2.0)), moveX=True, a=True)
                cmds.rotate(90, rotateX=True, a=True)
                roundedBlock = cmds.polyBoolOp(roundedBlock[0], finalCyl[0], ch=False, op=2)
            j=j+1
        cmds.rename(roundedBlock[0], dimension)      
        if dimension == 'height': 
            if extraBend == True:
                beamWidth = math.sqrt((1.6*1.6)*2)
                
                beam = cmds.polyCube(h=cubeY, w=beamWidth, d=cubeZ, sx=subdivisons)
       
                cylinder1 =  cmds.polyCylinder(r=0.38, h=cubeZ)
                cmds.move((beamWidth/2), moveX=True, a=True)
                cmds.rotate(90, rotateX=True, a=True)
                beam = cmds.polyBoolOp(beam[0], cylinder1[0], ch=False, op=1)
                
                cylinder2 =  cmds.polyCylinder(r=0.38, h=cubeZ)
                cmds.move((-beamWidth/2), moveX=True, a=True)
                cmds.rotate(90, rotateX=True, a=True)
                beam = cmds.polyBoolOp(beam[0], cylinder2[0], ch=False, op=1)
                
                cmds.move( beamWidth*0.5, moveX=True, r=True)            
                cmds.rotate(angle, rotateZ=True, ws=True, pivot=[0,0,0])           
                cmds.move( ((dimensions['length']*0.8)/2)-0.4, moveX=True, r=True)   
                
                beam = cmds.polyBoolOp(namespace_tmp+":length", beam[0], ch=False, op=1)       
                cmds.select(namespace_tmp+":height")
                
                moveLength = (dimensions['length']*0.8)*0.5 + 1.2 
                cmds.move( moveLength, moveX=True, r=True)           
                cmds.rotate(90, rotateZ=True, a=True)           
               
                cmds.move(1.2 + (dimensions['height']*0.8)*0.5, moveY=True, r=True)
                beam = cmds.polyBoolOp(namespace_tmp+":height", beam[0], ch=False, op=1)    
                
                #bottom corner inner hole
                littleCyl = cmds.polyCylinder(r=0.25, h=cubeZ)
                bigCyl1 = cmds.polyCylinder(r=0.32, h=0.09)
                cmds.move((cubeZ/2), moveY=True, a=True)
                littleCyl = cmds.polyBoolOp(bigCyl1[0], littleCyl[0], ch=False, op=1)
                
                bigCyl2 = cmds.polyCylinder(r=0.32, h=0.09)
                cmds.move((-cubeZ/2), moveY=True, a=True)
                finalCyl = cmds.polyBoolOp(bigCyl2[0], littleCyl[0], ch=False, op=1)                     
                cmds.move(cubeX*0.5, moveX=True, a=True)
                cmds.rotate(90, rotateX=True, a=True)
                
                cmds.move((dimensions['length']*0.8)*0.5 - 0.4, moveX=True, a=True)
                beam = cmds.polyBoolOp(beam[0], finalCyl[0], ch=False, op=2)   
                
                #top corner hole
                littleCyl = cmds.polyCylinder(r=0.25, h=cubeZ)
                bigCyl1 = cmds.polyCylinder(r=0.32, h=0.09)
                cmds.move((cubeZ/2), moveY=True, a=True)
                littleCyl = cmds.polyBoolOp(bigCyl1[0], littleCyl[0], ch=False, op=1)
                
                bigCyl2 = cmds.polyCylinder(r=0.32, h=0.09)
                cmds.move((-cubeZ/2), moveY=True, a=True)
                finalCyl = cmds.polyBoolOp(bigCyl2[0], littleCyl[0], ch=False, op=1)                     
                cmds.move(cubeX*0.5, moveX=True, a=True)
                cmds.rotate(90, rotateX=True, a=True)
                
                cmds.move((dimensions['length']*0.8)*0.5 + 1.2, moveX=True, a=True)
                cmds.move(1.6, moveY=True, a=True)
                beam = cmds.polyBoolOp(beam[0], finalCyl[0], ch=False, op=2)   
            else:
                cmds.move( ((dimensions['height']*0.8)/2)-0.4, moveX=True, r=True)            
                cmds.rotate(angle, rotateZ=True, ws=True, pivot=[0,0,0])           
                cmds.move( ((dimensions['length']*0.8)/2) - 0.4, moveX=True, r=True)   
                cmds.polyBoolOp(namespace_tmp+":length", namespace_tmp+":height", ch=False, op=1)        

    myShader = cmds.shadingNode('lambert', asShader=True, name="blockMaterial")       
    cmds.setAttr(namespace_tmp+":blockMaterial.color", rgb[0], rgb[1], rgb[2], type='double3')
    cmds.select(namespace_tmp+":*")
    cmds.delete(ch=True)
    
    cmds.hyperShade(assign=(namespace_tmp+":blockMaterial"))
    cmds.namespace(set=":")

def WheelAndHub():
    
    rnd = random.randrange(0,1000)
    namespace_tmp = "Hub_"+str(rnd)
    cmds.select(clear=True)
    cmds.namespace(add=namespace_tmp)
    cmds.namespace(set=namespace_tmp)
    
    axelHeight = 0.5
    axelWidth = axelHeight/3
    axelDepth = 1.6
    
    #Creating the hub
    outerHubCyl1 = cmds.polyCylinder(r=2.2, h=0.15, sx=40)
    innerHubCyl1 = cmds.polyCylinder(r=1.95, h=0.15, sx=40) 
    hubCyl1 = cmds.polyBoolOp(outerHubCyl1[0], innerHubCyl1[0], ch=False, op=2)
    
    outerHubCyl2 = cmds.polyCylinder(r=2.125, h=0.25, sx=40)
    innerHubCyl2 = cmds.polyCylinder(r=1.95, h=0.25, sx=40) 
    hubCyl2 = cmds.polyBoolOp(outerHubCyl2[0], innerHubCyl2[0], ch=False, op=2)
    cmds.move( -( (0.15/2) + (0.25/2) ), moveY=True, a=True)
    
    outerHubCyl3 = cmds.polyCylinder(r=2.2, h=0.11, sx=40)
    innerHubCyl3 = cmds.polyCylinder(r=1.95, h=0.11, sx=40) 
    hubCyl3 = cmds.polyBoolOp(outerHubCyl3[0], innerHubCyl3[0], ch=False, op=2) 
    cmds.move( -( (0.15/2) + 0.25 + (0.11/2) ), moveY=True, a=True)
    
    outerHubCyl4 = cmds.polyCylinder(r=2.125, h=0.15, sx=40)
    innerHubCyl4 = cmds.polyCylinder(r=1.95, h=0.15, sx=40) 
    hubCyl4 = cmds.polyBoolOp(outerHubCyl4[0], innerHubCyl4[0], ch=False, op=2)
    cmds.move( -( (0.15/2) + 0.25 + 0.11 + (0.15/2) ), moveY=True, a=True)   
    
    outerHubCyl5 = cmds.polyCylinder(r=2.125, h=0.01, sx=40)
    innerHubCyl5 = cmds.polyCylinder(r=1.725, h=0.01, sx=40) 
    hubCyl5 = cmds.polyBoolOp(outerHubCyl5[0], innerHubCyl5[0], ch=False, op=2)
    cmds.move( -( (0.15/2) + 0.25 + 0.11 + 0.15 + (0.01/2) ), moveY=True, a=True)   
    
    outerHubCyl6 = cmds.polyCylinder(r=1.725, h=0.3, sx=40)
    innerHubCyl6 = cmds.polyCylinder(r=1.5, h=0.3, sx=40) 
    hubCyl6 = cmds.polyBoolOp(outerHubCyl6[0], innerHubCyl6[0], ch=False, op=2)
    cmds.move( -( (0.15/2) + 0.25 + 0.11 + 0.16 + (0.3/2) ), moveY=True, a=True)   
    hubPiece1 = cmds.polyUnite((namespace_tmp+":*"), n=namespace_tmp, ch=False)
    cmds.duplicate(hubPiece1[0])
    cmds.scale(1,-1,1)
    cmds.move(-1.79, moveY=True, a=True)      
    OuterPiece = cmds.polyUnite((namespace_tmp+":*"), n=namespace_tmp, ch=False)
    
    cmds.move(1.569, moveY=True, r=True) 
    cmds.scale(1.7524, scaleY=True, r=True)   
    cmds.scale(1.023, scaleX=True, r=True)
    cmds.scale(1.023, scaleZ=True, r=True)
        
    axelCyl = cmds.polyCylinder(r=0.25, h=0.8)
    cmds.rotate(90, rotateX=True, a=True)
    
    veticalRect = cmds.polyCube(h=axelHeight, w=axelWidth, d=axelDepth)
    horizonalRect = cmds.polyCube(h=axelHeight, w=axelWidth, d=axelDepth)
    cmds.rotate(90, rotateZ=True, a=True)
    axel = cmds.polyBoolOp(veticalRect[0], horizonalRect[0], ch=False, op=1)
    axel = cmds.polyBoolOp(axel[0], axelCyl[0], ch=False, op=3)
    
    MiddleCyl = cmds.polyCylinder(r=0.32, h=0.8)
    cmds.rotate(90, rotateX=True, a=True)
    
    MiddleCyl = cmds.polyBoolOp(MiddleCyl[0], axel[0], ch=False, op=2)
    cmds.rotate(90, rotateX=True, a=True)
    
    x=1
    while x < 7:
        bigCyl = cmds.polyCylinder(r=0.32, h=0.4)
        littleCyl = cmds.polyCylinder(r=0.25, h=0.4)
        OuterCyl = cmds.polyBoolOp(bigCyl[0], littleCyl[0], name='OuterCyl'+str(x), ch=False, op=2)
        cmds.move((0.64 + 0.05), moveX=True, a=True)
        
        littleRect=cmds.polyCube(w=0.15, h=0.4, d=0.09)
        cmds.move((0.355), moveX=True, a=True)
        OuterCyl = cmds.polyBoolOp(littleRect[0], OuterCyl[0], ch=False, op=1)
        
        bigRect=cmds.polyCube(w=0.5, h=0.4, d=0.09)
        cmds.move((1.25), moveX=True, a=True)
        OuterCyl = cmds.polyBoolOp(bigRect[0], OuterCyl[0], ch=False, op=1)
        
        littleRect=cmds.polyCube(w=0.15, h=0.4, d=0.09)
        cmds.move(0.5, moveX=True)
        cmds.move(0.3, moveZ=True)
        cmds.rotate(60, rotateY=True)
        OuterCyl = cmds.polyBoolOp(littleRect[0], OuterCyl[0], ch=False, op=1)
        cmds.rotate((60*x), rotateY=True, pivot=[0,0,0])
        
        MiddleCyl = cmds.polyBoolOp(MiddleCyl[0], OuterCyl[0], ch=False, op=1)
        x=x+1  
    
    hub = cmds.polyUnite(OuterPiece[0], MiddleCyl[0], ch=False) 
        
    #Creating the wheel
    wheelSphere = cmds.polySphere(r=3.3, sx=40, sy=10)
    wheelCyl = cmds.polyCylinder(r=3.25, sx=40, sy=2, h=3.4)
            
    baseWheel = cmds.polyBoolOp(wheelSphere[0], wheelCyl[0], ch=False, op=3)
    
    wheelCylNotchEndSmall = cmds.polyCylinder(r=3.0, sx=40, h=0.523)
    cmds.select(str(wheelCylNotchEndSmall[0])+'.f[41]')
    cmds.scale(0.75, scaleX=True, a=True)
    cmds.scale(0.75, scaleZ=True, a=True)
    wheelCylNotchEndBig = cmds.polyCylinder(r=4.0, h=0.523)
    wheelCylNotchEnd = cmds.polyBoolOp(wheelCylNotchEndBig[0], wheelCylNotchEndSmall[0], ch=False, op=2)
    cmds.move(1.053 + (0.25/2) + (0.523/2), moveY=True, a=True)
    baseWheel = cmds.polyBoolOp(baseWheel[0], wheelCylNotchEnd[0], ch=False, op=2)
    
    wheelCylNotchEndSmall = cmds.polyCylinder(r=3.0, sx=40, h=0.523)
    cmds.select(str(wheelCylNotchEndSmall[0])+'.f[40]')
    cmds.scale(0.75, scaleX=True, a=True)
    cmds.scale(0.75, scaleZ=True, a=True)
    wheelCylNotchEndBig = cmds.polyCylinder(r=4.0, h=0.523)
    wheelCylNotchEnd = cmds.polyBoolOp(wheelCylNotchEndBig[0], wheelCylNotchEndSmall[0], ch=False, op=2)
    cmds.move(-(1.053 + (0.25/2) + (0.523/2)), moveY=True, a=True)
    baseWheel = cmds.polyBoolOp(baseWheel[0], wheelCylNotchEnd[0], ch=False, op=2)
    
    wheelCylNotchSmall = cmds.polyCylinder(r=3.0, sx=40, h=0.25)
    cmds.select(str(wheelCylNotchSmall[0])+'.f[40]')
    cmds.scale(1.02, scaleX=True, a=True)
    cmds.scale(1.02, scaleZ=True, a=True)
    wheelCylNotchBig = cmds.polyCylinder(r=3.5, h=0.25)
    baseWheelNotchCyl = cmds.polyBoolOp(wheelCylNotchBig[0], wheelCylNotchSmall[0], ch=False, op=2)
    cmds.move(1.053, moveY=True, a=True)
    baseWheel = cmds.polyBoolOp(baseWheel[0], baseWheelNotchCyl[0], ch=False, op=2)
    
    wheelCylNotchSmall = cmds.polyCylinder(r=3.0, sx=40, h=0.25)
    cmds.select(str(wheelCylNotchSmall[0])+'.f[41]')
    cmds.scale(1.02, scaleX=True, a=True)
    cmds.scale(1.02, scaleZ=True, a=True)
    wheelCylNotchBig = cmds.polyCylinder(r=3.5, h=0.25)
    baseWheelNotchCyl = cmds.polyBoolOp(wheelCylNotchBig[0], wheelCylNotchSmall[0], ch=False, op=2)
    cmds.move(-1.053, moveY=True, a=True)
    baseWheel = cmds.polyBoolOp(baseWheel[0], baseWheelNotchCyl[0], ch=False, op=2)
    
    for x in range(21):    
        notchCube = cmds.polyCube(w=0.4, d=2.0, h=1.86)   
        cmds.move(-3.533, moveZ=True)
        cmds.move(1.521, moveY=True)#- (3.042 * i)
        cmds.rotate(35.714, rotateX=True) #- (i*71.428)
        cmds.rotate(x*18, rotateY=True, ws=True, pivot=[0, 0, 0])#+(i*0.5))
        baseWheel = cmds.polyBoolOp(baseWheel[0], notchCube[0], ch=False, op=2)       
    
    cmds.select(baseWheel[0]+'.f[49:89]')
    cmds.select(baseWheel[0]+'.f[131:210]', add=True)
    cmds.delete(ch=False)
    cmds.select(str(baseWheel[0])+'.f[211:251]', add=True)
    cmds.delete(ch=False)
    
    cmds.select(baseWheel[0])
    baseWheelBottom = cmds.duplicate()
    cmds.scale(-1, scaleY=True, a=True)
    cmds.rotate(-27, rotateY=True, a=True)    
    
    tire = cmds.polyUnite(baseWheelBottom[0], baseWheel[0], n=namespace_tmp, ch=False)
    cutOutCen = cmds.polyCylinder(r=2.2514345, h=4.0, sx=40)
    tire = cmds.polyBoolOp(tire[0], cutOutCen[0], ch=False, op=2)    
    
    myShader = cmds.shadingNode('lambert', asShader=True, name="tireMaterial")
    cmds.select(tire[0])
    cmds.setAttr(namespace_tmp+":tireMaterial.color", 0.08, 0.08, 0.08, type='double3')
    cmds.hyperShade(assign=(namespace_tmp+":tireMaterial"))
    
    myShader = cmds.shadingNode('lambert', asShader=True, name="hubMaterial")
    cmds.select(hub[0])
    cmds.setAttr(namespace_tmp+":hubMaterial.color", 0.6, 0.6, 0.6, type='double3')
    cmds.hyperShade(assign=(namespace_tmp+":hubMaterial"))
    
    wheel = cmds.polyUnite(tire[0], hub[0], ch=False)
    cmds.namespace(set=":")

def Connectors():
    blackConnecter = cmds.checkBox('blackConnecter', query=True, value=True)
    blueConnecter = cmds.checkBox('blueConnecter', query=True, value=True)
    blackDoubleConnecter = cmds.checkBox('blackDoubleConnecter', query=True, value=True)
    
    blackSpacerConnecter = cmds.checkBox('blackSpacerConnecter', query=True, value=True)
    greySpacer = cmds.checkBox('greySpacer', query=True, value=True)
    greyDoubleSpacer = cmds.checkBox('greyDoubleSpacer', query=True, value=True)
    
    axelDoubleSpacer = cmds.checkBox('axelDoubleSpacer', query=True, value=True)
    redAxelConnector = cmds.checkBox('redAxelConnector', query=True, value=True)
    longBallConnector = cmds.checkBox('longBallConnector', query=True, value=True)
    
    greyHalfConnector = cmds.checkBox('greyHalfConnector', query=True, value=True)
    ballAxelConnector = cmds.checkBox('ballAxelConnector', query=True, value=True)
    DoubleSpacerHole = cmds.checkBox('DoubleSpacerHole', query=True, value=True)
    
    rnd = random.randrange(0,10000)
    namespace_tmp = "Connectors_"+str(rnd)
    cmds.select(clear=True)
    cmds.namespace(add=namespace_tmp)
    cmds.namespace(set=namespace_tmp)
    
    if blackConnecter==True:
        littleCyl = cmds.polyCylinder(r=0.25, h=0.71)
        bigCyl1 = cmds.polyCylinder(r=0.32, h=0.09)
        cmds.move((0.71*0.5) +(0.09*0.5), moveY=True, a=True)
        mainCyl = cmds.polyBoolOp(bigCyl1[0], littleCyl[0], ch=False, op=1)
        littleCyl = cmds.polyCylinder(r=0.25, h=0.71)
        cmds.move(0.8, moveY=True, a=True)
        mainCyl = cmds.polyBoolOp(mainCyl[0], littleCyl[0], ch=False, op=1)
        
        cutOutTop = cmds.polyCube(w=0.8, h=0.4, d=0.1)
        cmds.move(1.0, moveY=True, a=True)
        connector = cmds.polyBoolOp(mainCyl[0], cutOutTop[0], ch=False, op=2)
        
        cutOutBottom = cmds.polyCube(w=0.8, h=0.4, d=0.1)
        cmds.move(-0.2, moveY=True, a=True)
        connector = cmds.polyBoolOp(connector[0], cutOutBottom[0], ch=False, op=2)
        
        cutOutCyl = cmds.polyCylinder(r=0.20, h=3.0)
        connector = cmds.polyBoolOp(connector[0], cutOutCyl[0], ch=False, op=2)
        
        myShader = cmds.shadingNode('lambert', asShader=True, name="blackMaterial")
        cmds.setAttr(namespace_tmp+":blackMaterial.color", 0.05, 0.05, 0.05, type='double3')
        cmds.select(connector[0])
        cmds.delete(ch=True)
        cmds.hyperShade(assign=(namespace_tmp+":blackMaterial"))
        
    if blueConnecter==True:
        #connector side
        littleCyl = cmds.polyCylinder(r=0.25, h=0.71)
        bigCyl1 = cmds.polyCylinder(r=0.32, h=0.045)
        cmds.move((0.71*0.5) +(0.045*0.5), moveY=True, a=True)
        mainCyl = cmds.polyBoolOp(bigCyl1[0], littleCyl[0], ch=False, op=1)
        
        cutOutBottom = cmds.polyCube(w=0.8, h=0.4, d=0.1)
        cmds.move(-0.2, moveY=True, a=True)
        connector = cmds.polyBoolOp(mainCyl[0], cutOutBottom[0], ch=False, op=2)
        
        cutOutCyl = cmds.polyCylinder(r=0.20, h=0.8)
        connector = cmds.polyBoolOp(connector[0], cutOutCyl[0], ch=False, op=2)
        
        #axel side        
        height = 0.5
        width = height/3
        depth = 0.8
        
        cyl = cmds.polyCylinder(r=0.25, h=depth)
        cmds.rotate(90, rotateX=True, a=True)
        
        veticalRect = cmds.polyCube(h=height, w=width, d=depth)
        horizonalRect = cmds.polyCube(h=height, w=width, d=depth)
        cmds.rotate(90, rotateZ=True, a=True)
        axel = cmds.polyBoolOp(veticalRect[0], horizonalRect[0], ch=False, op=1)
        axel = cmds.polyBoolOp(axel[0], cyl[0], ch=False, op=3)
        cmds.rotate(90, rotateX=True, a=True)
        cmds.move(0.8, moveY=True, a=True)
        blueConnector = cmds.polyBoolOp(connector[0], axel[0], ch=False, op=1)
        
        myShader = cmds.shadingNode('lambert', asShader=True, name="blueMaterial")
        cmds.setAttr(namespace_tmp+":blueMaterial.color", 0, 0, 1, type='double3')
        cmds.select(blueConnector[0])
        cmds.delete(ch=True)
        cmds.hyperShade(assign=(namespace_tmp+":blueMaterial"))

    if blackSpacerConnecter==True:
        #create spacer
        littleCyl = cmds.polyCylinder(r=0.28, h=0.71)
        bigCyl1 = cmds.polyCylinder(r=0.32, h=0.045)
        cmds.move((0.71*0.5) + (0.045*0.5), moveY=True, a=True)
        littleCyl = cmds.polyBoolOp(bigCyl1[0], littleCyl[0], ch=False, op=1)
        
        bigCyl2 = cmds.polyCylinder(r=0.32, h=0.09)
        cmds.move((-0.71*0.5) - (0.09*0.5), moveY=True, a=True)
        finalCyl = cmds.polyBoolOp(bigCyl2[0], littleCyl[0], ch=False, op=1)                     
        cmds.rotate(90, rotateX=True, a=True)
        height = 0.5
        width = height/3
        depth = 1.0
        
        cyl = cmds.polyCylinder(r=0.25, h=depth)
        cmds.rotate(90, rotateX=True, a=True)
        
        veticalRect = cmds.polyCube(h=height, w=width, d=depth) 
        horizonalRect = cmds.polyCube(h=height, w=width, d=depth)
        cmds.rotate(90, rotateZ=True, a=True)
        axel = cmds.polyBoolOp(veticalRect[0], horizonalRect[0], ch=False, op=1)
        axel = cmds.polyBoolOp(axel[0], cyl[0], ch=False, op=3)
        blackDoubleSpacer = cmds.polyBoolOp(finalCyl[0], axel[0], ch=False, op=2)
        cmds.rotate(90, rotateX=True, a=True)
        
        #create double connector side
        littleCyl = cmds.polyCylinder(r=0.25, h=0.755+0.8)
        cmds.move(1.177, moveY=True, a=True)
        mainCyl = cmds.polyBoolOp(blackDoubleSpacer[0], littleCyl[0], ch=False, op=1)
        cutOutTop = cmds.polyCube(w=0.8, h=0.4, d=0.1)
        cmds.move(1.755, moveY=True, a=True)

        connector = cmds.polyBoolOp(mainCyl[0], cutOutTop[0], ch=False, op=2)
        cutOutCyl = cmds.polyCylinder(r=0.20, h=2.5)
        cmds.move(1.673, moveY=True, a=True)
        blackDoubleConnecter = cmds.polyBoolOp(connector[0], cutOutCyl[0], ch=False, op=2)
        
        myShader = cmds.shadingNode('lambert', asShader=True, name="blackMaterial")
        cmds.setAttr(namespace_tmp+":blackMaterial.color", 0.05, 0.05, 0.05, type='double3')
        cmds.select(blackDoubleConnecter[0])
        cmds.delete(ch=True)
        cmds.hyperShade(assign=(namespace_tmp+":blackMaterial"))
        
    if blackDoubleConnecter==True:
        littleCyl = cmds.polyCylinder(r=0.25, h=0.71)
        bigCyl1 = cmds.polyCylinder(r=0.32, h=0.09)
        cmds.move((0.71*0.5)+ 0.09*0.5, moveY=True, a=True)
        mainCyl = cmds.polyBoolOp(bigCyl1[0], littleCyl[0], ch=False, op=1)
        
        littleCyl = cmds.polyCylinder(r=0.25, h=0.71+0.8)
        cmds.move(1.2, moveY=True, a=True)

        mainCyl = cmds.polyBoolOp(mainCyl[0], littleCyl[0], ch=False, op=1)
        cutOutTop = cmds.polyCube(w=0.8, h=0.4, d=0.1)
        cmds.move(1.8, moveY=True, a=True)
        connector = cmds.polyBoolOp(mainCyl[0], cutOutTop[0], ch=False, op=2)
        
        cutOutBottom = cmds.polyCube(w=0.8, h=0.4, d=0.1)
        cmds.move(-0.2, moveY=True, a=True)
        connector = cmds.polyBoolOp(connector[0], cutOutBottom[0], ch=False, op=2)
        
        cutOutCyl = cmds.polyCylinder(r=0.20, h=5.0)
        blackDoubleConnecter = cmds.polyBoolOp(connector[0], cutOutCyl[0], ch=False, op=2)
        
        myShader = cmds.shadingNode('lambert', asShader=True, name="blackMaterial")
        cmds.setAttr(namespace_tmp+":blackMaterial.color", 0.05, 0.05, 0.05, type='double3')
        cmds.select(blackDoubleConnecter[0])
        cmds.delete(ch=True)
        cmds.hyperShade(assign=(namespace_tmp+":blackMaterial"))
        
    if greySpacer==True:
        littleCyl = cmds.polyCylinder(r=0.28, h=0.71*0.5)
        bigCyl1 = cmds.polyCylinder(r=0.32, h=0.045)
        cmds.move((0.71/2)*0.5, moveY=True, a=True)
        littleCyl = cmds.polyBoolOp(bigCyl1[0], littleCyl[0], ch=False, op=1)
        
        bigCyl2 = cmds.polyCylinder(r=0.32, h=0.045)
        cmds.move((-0.71/2)*0.5, moveY=True, a=True)
        finalCyl = cmds.polyBoolOp(bigCyl2[0], littleCyl[0], ch=False, op=1)                     
        cmds.rotate(90, rotateX=True, a=True)
        
        height = 0.5
        width = height/3
        depth = 1.0
        
        cyl = cmds.polyCylinder(r=0.25, h=depth)
        cmds.rotate(90, rotateX=True, a=True)
        
        veticalRect = cmds.polyCube(h=height, w=width, d=depth)
        horizonalRect = cmds.polyCube(h=height, w=width, d=depth)
        cmds.rotate(90, rotateZ=True, a=True)
        axel = cmds.polyBoolOp(veticalRect[0], horizonalRect[0], ch=False, op=1)
        axel = cmds.polyBoolOp(axel[0], cyl[0], ch=False, op=3)
        
        greySpacer = cmds.polyBoolOp(finalCyl[0], axel[0], ch=False, op=2)
        
        myShader = cmds.shadingNode('lambert', asShader=True, name="greyMaterial")
        cmds.setAttr(namespace_tmp+":greyMaterial.color", 0.6, 0.6, 0.6, type='double3')
        cmds.select(greySpacer[0])
        cmds.delete(ch=True)
        cmds.hyperShade(assign=(namespace_tmp+":greyMaterial"))
    
    if greyDoubleSpacer==True:
        littleCyl = cmds.polyCylinder(r=0.28, h=0.71)
        bigCyl1 = cmds.polyCylinder(r=0.32, h=0.045)
        cmds.move((0.71*0.5) +(0.045*0.5), moveY=True, a=True)
        littleCyl = cmds.polyBoolOp(bigCyl1[0], littleCyl[0], ch=False, op=1)
        
        bigCyl2 = cmds.polyCylinder(r=0.32, h=0.045)
        cmds.move((-0.71*0.5)-(0.045*0.5), moveY=True, a=True)
        finalCyl = cmds.polyBoolOp(bigCyl2[0], littleCyl[0], ch=False, op=1)                     
        cmds.rotate(90, rotateX=True, a=True)
        
        height = 0.5
        width = height/3
        depth = 1.0
        
        cyl = cmds.polyCylinder(r=0.25, h=depth)
        cmds.rotate(90, rotateX=True, a=True)
        
        veticalRect = cmds.polyCube(h=height, w=width, d=depth)
        horizonalRect = cmds.polyCube(h=height, w=width, d=depth)
        cmds.rotate(90, rotateZ=True, a=True)
        axel = cmds.polyBoolOp(veticalRect[0], horizonalRect[0], ch=False, op=1)
        axel = cmds.polyBoolOp(axel[0], cyl[0], ch=False, op=3)
        
        greyDoubleSpacer = cmds.polyBoolOp(finalCyl[0], axel[0], ch=False, op=2)
        
        myShader = cmds.shadingNode('lambert', asShader=True, name="greyMaterial")
        cmds.setAttr(namespace_tmp+":greyMaterial.color", 0.6, 0.6, 0.6, type='double3')
        cmds.select(greyDoubleSpacer[0])
        cmds.delete(ch=True)
        cmds.hyperShade(assign=(namespace_tmp+":greyMaterial"))
            
    if axelDoubleSpacer==True:
        #spacer
        littleCyl = cmds.polyCylinder(r=0.28, h=0.71)
        bigCyl1 = cmds.polyCylinder(r=0.32, h=0.045)
        cmds.move((0.71*0.5) +(0.045*0.5), moveY=True, a=True)
        littleCyl = cmds.polyBoolOp(bigCyl1[0], littleCyl[0], ch=False, op=1)
        
        bigCyl2 = cmds.polyCylinder(r=0.32, h=0.045)
        cmds.move((-0.71*0.5) - (0.045*0.5), moveY=True, a=True)
        finalCyl = cmds.polyBoolOp(bigCyl2[0], littleCyl[0], ch=False, op=1)                     
        
        height = 0.5
        width = height/3
        depth = 1.0
        
        cyl = cmds.polyCylinder(r=0.25, h=depth)
        cmds.rotate(90, rotateX=True, a=True)
        veticalRect = cmds.polyCube(h=height, w=width, d=depth)
        horizonalRect = cmds.polyCube(h=height, w=width, d=depth)
        cmds.rotate(90, rotateZ=True, a=True)
        axel = cmds.polyBoolOp(veticalRect[0], horizonalRect[0], ch=False, op=1)
        axel = cmds.polyBoolOp(axel[0], cyl[0], ch=False, op=3)
        cmds.rotate(90, rotateX=True, a=True)
        
        connectingCube = cmds.polyCube(w=0.5, h=0.8, d=0.5)
        cmds.move(-0.447, moveZ=True, a=True)
        
        DoubleSpacer = cmds.polyBoolOp(connectingCube[0], finalCyl[0], ch=False, op=1)
        DoubleSpacer = cmds.polyBoolOp(DoubleSpacer[0], axel[0], ch=False, op=2)

        #axel side        
        height = 0.5
        width = height/3
        depth = 1.2
        
        cyl = cmds.polyCylinder(r=0.25, h=depth)
        cmds.rotate(90, rotateX=True, a=True)
        
        veticalRect = cmds.polyCube(h=height, w=width, d=depth)
        horizonalRect = cmds.polyCube(h=height, w=width, d=depth)
        cmds.rotate(90, rotateZ=True, a=True)
        axel = cmds.polyBoolOp(veticalRect[0], horizonalRect[0], ch=False, op=1)
        axel = cmds.polyBoolOp(axel[0], cyl[0], ch=False, op=3)
        cmds.move(-1.297, moveZ=True, a=True)
        
        myShader = cmds.shadingNode('lambert', asShader=True, name="blackMaterial")
        cmds.setAttr(namespace_tmp+":blackMaterial.color", 0.05, 0.05, 0.05, type='double3')
        blackDoubleSpacer = cmds.polyBoolOp(DoubleSpacer[0], axel[0], ch=False, op=1)
        cmds.delete(ch=True)
        cmds.hyperShade(assign=(namespace_tmp+":blackMaterial"))      
       
    if redAxelConnector==True: 
        #axel side        
        height = 0.5
        width = height/3
        depth = 1.5
        
        cyl = cmds.polyCylinder(r=0.32, h=depth)
        cmds.rotate(90, rotateX=True, a=True)
        
        veticalRect = cmds.polyCube(h=height, w=width, d=depth)
        horizonalRect = cmds.polyCube(h=height, w=width, d=depth)
        cmds.rotate(90, rotateZ=True, a=True)
        axel = cmds.polyBoolOp(veticalRect[0], horizonalRect[0], ch=False, op=1)
        axel = cmds.polyBoolOp(axel[0], cyl[0], ch=False, op=3)
        
        cylBig = cmds.polyCylinder(r=0.27, h=0.1)
        cylSmall = cmds.polyCylinder(r=0.2, h=0.1)
        cyl = cmds.polyBoolOp(cylBig[0], cylSmall[0], ch=False, op=2)
        cmds.rotate(90, rotateX=True, a=True)
        cmds.move(0.75 - 0.3, moveZ=True, a=True)
        
        cyl2 = cmds.duplicate()
        cmds.move( -(0.75 - 0.3), moveZ=True, a=True)
        cyl = cmds.polyUnite(cyl[0], cyl2[0], ch=False)
        
        myShader = cmds.shadingNode('lambert', asShader=True, name="redMaterial")
        cmds.setAttr(namespace_tmp+":redMaterial.color", 1, 0.04, 0.04, type='double3')
        cmds.polyBoolOp(axel[0], cyl[0], ch=False, op=2)
        cmds.delete(ch=True)
        cmds.hyperShade(assign=(namespace_tmp+":redMaterial"))     
         
    if longBallConnector==True: 
        height = 0.5
        width = height/3
        depth = 4*0.8
        
        #end cylinders
        bigCyl1 = cmds.polyCylinder(r=0.32, h=0.5)
        cmds.move(-(depth*0.5) - 0.195, moveZ=True, a=True)
        
        bigCyl2 = cmds.polyCylinder(r=0.32, h=0.5)
        cmds.move( (depth*0.5) + 0.195, moveZ=True, a=True)
        
        bigCyls = cmds.polyUnite(bigCyl1[0], bigCyl2[0], ch=False)
        
        littleCyl1 = cmds.polyCylinder(r=0.25, h=0.5)
        cmds.move(-(depth*0.5) - 0.195, moveZ=True, a=True)
        
        littleCyl2 = cmds.polyCylinder(r=0.25, h=0.5)
        cmds.move((depth*0.5) + 0.195, moveZ=True, a=True)
        
        littleCyls = cmds.polyUnite(littleCyl1[0], littleCyl2[0], ch=False)   
        
        #axel piece                            
        cyl = cmds.polyCylinder(r=0.25, h=depth)
        cmds.rotate(90, rotateX=True, a=True)
        
        veticalRect = cmds.polyCube(h=height, w=width, d=depth)
        horizonalRect = cmds.polyCube(h=height, w=width, d=depth)
        cmds.rotate(90, rotateZ=True, a=True)
        axel = cmds.polyBoolOp(veticalRect[0], horizonalRect[0], ch=False, op=1)
        axel = cmds.polyBoolOp(axel[0], cyl[0], ch=False, op=3)
        longBallConnector = cmds.polyBoolOp(axel[0], bigCyls[0], ch=False, op=1)

        myShader = cmds.shadingNode('lambert', asShader=True, name="blackMaterial")
        cmds.setAttr(namespace_tmp+":blackMaterial.color", 0.08, 0.08, 0.08, type='double3')
        longBallConnector = cmds.polyBoolOp(longBallConnector[0], littleCyls[0], ch=False, op=2)
        cmds.delete(ch=True)
        cmds.hyperShade(assign=(namespace_tmp+":blackMaterial"))    
        
    if greyHalfConnector==True:
        littleCyl = cmds.polyCylinder(r=0.25, h=0.71)
        bigCyl1 = cmds.polyCylinder(r=0.32, h=0.09)
        cmds.move((0.71*0.5) + (0.09*0.5), moveY=True, a=True)
        mainCyl = cmds.polyBoolOp(bigCyl1[0], littleCyl[0], ch=False, op=1)
        littleCyl = cmds.polyCylinder(r=0.25, h=0.4)
        cmds.move(0.645, moveY=True, a=True)
        
        mainCyl = cmds.polyBoolOp(mainCyl[0], littleCyl[0], ch=False, op=1)
        cutOutTop = cmds.polyCube(w=0.8, h=0.4, d=0.1)
        cmds.move(0.7, moveY=True, a=True)
        connector = cmds.polyBoolOp(mainCyl[0], cutOutTop[0], ch=False, op=2)
        
        cutOutBottom = cmds.polyCube(w=0.8, h=0.4, d=0.1)
        cmds.move(-0.2, moveY=True, a=True)
        connector = cmds.polyBoolOp(connector[0], cutOutBottom[0], ch=False, op=2)
        
        cutOutCyl = cmds.polyCylinder(r=0.20, h=3.0)
        connector = cmds.polyBoolOp(connector[0], cutOutCyl[0], ch=False, op=2)
        
        myShader = cmds.shadingNode('lambert', asShader=True, name="greyMaterial")
        cmds.setAttr(namespace_tmp+":greyMaterial.color", 0.6, 0.6, 0.6, type='double3')
        cmds.select(connector[0])
        cmds.delete(ch=True)
        cmds.hyperShade(assign=(namespace_tmp+":greyMaterial"))
        
    if ballAxelConnector==True:
        #ball side
        ball = cmds.polySphere(r=0.25)
        ballCyl = cmds.polyCylinder(r=0.15, h=0.15)
        cmds.move(0.25, moveY=True, a=True)
        ball = cmds.polyBoolOp(ball[0], ballCyl[0], ch=False, op=1)
        
        ballCyl = cmds.polyCylinder(r=0.32, h=0.045)
        cmds.move(0.345, moveY=True, a=True)
        ball = cmds.polyBoolOp(ball[0], ballCyl[0], ch=False, op=1)
        #axel side        
        height  = 0.5
        width = height/3
        depth = 0.8
        
        cyl = cmds.polyCylinder(r=0.25, h=depth)
        cmds.rotate(90, rotateX=True, a=True)
        
        veticalRect = cmds.polyCube(h=height, w=width, d=depth)
        horizonalRect = cmds.polyCube(h=height, w=width, d=depth)
        cmds.rotate(90, rotateZ=True, a=True)
        axel = cmds.polyBoolOp(veticalRect[0], horizonalRect[0], ch=False, op=1)
        axel = cmds.polyBoolOp(axel[0], cyl[0], ch=False, op=3)
        cmds.rotate(90, rotateX=True, a=True)
        cmds.move(0.768, moveY=True, a=True)
        myShader = cmds.shadingNode('lambert', asShader=True, name="greyMaterial")
        cmds.setAttr(namespace_tmp+":greyMaterial.color", 0.6, 0.6, 0.6, type='double3')
        ballConnector = cmds.polyBoolOp(ball[0], axel[0], ch=False, op=1)
        cmds.delete(ch=True)
        cmds.hyperShade(assign=(namespace_tmp+":greyMaterial"))
    if DoubleSpacerHole==True:
        #spacer
        littleCyl = cmds.polyCylinder(r=0.28, h=0.71)
        bigCyl1 = cmds.polyCylinder(r=0.4, h=0.045)
        cmds.move((0.71*0.5) + (0.045*0.5), moveY=True, a=True)
        littleCyl = cmds.polyBoolOp(bigCyl1[0], littleCyl[0], ch=False, op=1)
        
        bigCyl2 = cmds.polyCylinder(r=0.4, h=0.045)
        cmds.move((-0.71*0.5) - (0.045*0.5), moveY=True, a=True)
        finalCyl = cmds.polyBoolOp(bigCyl2[0], littleCyl[0], ch=False, op=1)                     
        
        height = 0.5
        width = height/3
        depth = 0.8
        
        cyl = cmds.polyCylinder(r=0.25, h=depth)
        cmds.rotate(90, rotateX=True, a=True)
        veticalRect = cmds.polyCube(h=height, w=width, d=depth)
        horizonalRect = cmds.polyCube(h=height, w=width, d=depth)
        cmds.rotate(90, rotateZ=True, a=True)
        axel = cmds.polyBoolOp(veticalRect[0], horizonalRect[0], ch=False, op=1)
        axel = cmds.polyBoolOp(axel[0], cyl[0], ch=False, op=3)
        cmds.rotate(90, rotateX=True, a=True)
        
        connectingCube = cmds.polyCube(w=0.8, h=0.8, d=0.8)
        cmds.move(-0.4, moveZ=True, a=True)
        
        DoubleSpacer = cmds.polyBoolOp(connectingCube[0], finalCyl[0], ch=False, op=1)
        DoubleSpacer = cmds.polyBoolOp(DoubleSpacer[0], axel[0], ch=False, op=2)
        #hole
        parentCyl = cmds.polyCylinder(r=0.4, h=0.8)
        cmds.rotate(90, rotateZ=True, a=True)
        cmds.move(-0.8, moveZ=True, a=True)
        parentCyl = cmds.polyBoolOp(parentCyl[0], DoubleSpacer[0], ch=False, op=1)
        
        littleCyl = cmds.polyCylinder(r=0.25, h=0.71)
        bigCyl1 = cmds.polyCylinder(r=0.32, h=0.045)
        cmds.move( (0.71*0.5) + 0.045*0.5, moveY=True, a=True)
        littleCyl = cmds.polyBoolOp(bigCyl1[0], littleCyl[0], ch=False, op=1)
        
        bigCyl2 = cmds.polyCylinder(r=0.32, h=0.09)
        cmds.move( (-0.71*0.5) - 0.045*0.5, moveY=True, a=True)
        finalCyl = cmds.polyBoolOp(bigCyl2[0], littleCyl[0], ch=False, op=1)                     
        cmds.move(-0.8, moveZ=True, a=True)
        cmds.rotate(90, rotateZ=True, a=True)
        DoubleSpacerHole = cmds.polyBoolOp(parentCyl[0], finalCyl[0], ch=False, op=2)
        myShader = cmds.shadingNode('lambert', asShader=True, name="Material")
        cmds.setAttr(namespace_tmp+":Material.color", 0.05, 0.05, 0.05, type='double3')
        cmds.select(DoubleSpacerHole[0])
        cmds.delete(ch=True)
        cmds.hyperShade(assign=(namespace_tmp+":Material"))
    cmds.namespace(set=":")
    
def Axel():
    axelLength = cmds.intSliderGrp('axelLength', query=True, value=True)
    stopper = cmds.checkBox('stopper', query=True, value=True)
    col = cmds.radioButtonGrp('axelColor', query=True, sl=True)
    print col 
    rnd = random.randrange(0,1000)
    namespace_tmp = "axel_"+str(rnd)
    cmds.select(clear=True)
    cmds.namespace(add=namespace_tmp)
    cmds.namespace(set=namespace_tmp)
    
    height = 0.5
    width = height/3
    depth = axelLength*0.8
    
    cyl = cmds.polyCylinder(r=0.25, h=depth)
    cmds.rotate(90, rotateX=True, a=True)
    
    veticalRect = cmds.polyCube(h=height, w=width, d=depth)
    horizonalRect = cmds.polyCube(h=height, w=width, d=depth)
    cmds.rotate(90, rotateZ=True, a=True)
    axel = cmds.polyBoolOp(veticalRect[0], horizonalRect[0], ch=False, op=1)
    axel = cmds.polyBoolOp(axel[0], cyl[0], ch=False, op=3)
    
    if stopper==True:
        bigCyl = cmds.polyCylinder(r=0.25, h=0.2)
        littleCyl = cmds.polyCylinder(r=0.15, h=0.2)
        nub = cmds.polyBoolOp(bigCyl[0], littleCyl[0], ch=False, op=2)
        cmds.rotate(90, rotateX=True, a=True)
        cmds.move((0.1 + depth*0.5) + 0.045, moveZ=True, a=True)
        
        bigCylOuter = cmds.polyCylinder(r=0.32, h=0.045)
        cmds.rotate(90, rotateX=True, a=True)
        cmds.move((depth*0.5) + (0.045*0.5), moveZ=True, a=True)
        axel = cmds.polyBoolOp(axel[0], bigCylOuter[0], ch=False, op=1)
        axel = cmds.polyBoolOp(axel[0], nub[0], ch=False, op=1)
    
    myShader = cmds.shadingNode('lambert', asShader=True, name="Material")
    if col == 1:
        cmds.setAttr(namespace_tmp+":Material.color", 0.6, 0.6, 0.6, type='double3')
    if col == 2:
        cmds.setAttr(namespace_tmp+":Material.color", 0.05, 0.05, 0.05, type='double3')
    cmds.select(axel[0])
    cmds.delete(ch=True)
    cmds.hyperShade(assign=(namespace_tmp+":Material"))
    cmds.namespace(set=":")
        
def basicBlock():
    height = cmds.intSliderGrp('blockHeight', query=True, value=True)
    width = cmds.intSliderGrp('blockWidth', query=True, value=True)
    depth = cmds.intSliderGrp('blockDepth', query=True, value=True)
    rgb = cmds.colorSliderGrp('basicBlockColour', query=True, rgbValue=True)
    
    rnd = random.randrange(0,1000)
    namespace_tmp = "basicBlock_"+str(rnd)
    cmds.select(clear=True)
    cmds.namespace(add=namespace_tmp)
    cmds.namespace(set=namespace_tmp)
    
    cubeSizeX = width * 0.8
    cubeSizeZ = depth * 0.8
    cubeSizeY = height * 0.32
    
    cmds.polyCube(h=cubeSizeY, w=cubeSizeX, d=cubeSizeZ)
    cmds.move((cubeSizeY/2.0), moveY=True, a=True)
    for i in range(width):
        for j in range(depth):
            cmds.polyCylinder(r=0.25, h=0.20)
            cmds.move((cubeSizeY + 0.1), moveY=True, a=True)
            cmds.move(((i*0.8) - (cubeSizeX/2.0) + 0.4), moveX=True, a=True)
            cmds.move(((j*0.8) - (cubeSizeZ/2.0) + 0.4), moveZ=True, a=True)
    
    myShader = cmds.shadingNode('lambert', asShader=True, name="blockMaterial")
    
    cmds.setAttr(namespace_tmp+":blockMaterial.color", rgb[0], rgb[1], rgb[2], type='double3')
    cmds.polyUnite((namespace_tmp+":*"), n=namespace_tmp, ch=False)
    cmds.delete(ch=True)
    
    cmds.hyperShade(assign=(namespace_tmp+":blockMaterial"))
    cmds.namespace(set=":")