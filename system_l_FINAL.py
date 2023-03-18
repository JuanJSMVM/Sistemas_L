import turtle as lia
import random    

def gen_cads(axiom, product_rules, n_items):
    new_axiom=axiom
    for _ in range(n_items):
        list_axiom=[]
        for car in new_axiom:
            aux=car
            if car in product_rules.keys():
                choose=random.choice(product_rules[car])
                list_axiom.extend(list(choose))
            else:    
                list_axiom.append(aux)
        new_axiom=''.join(list_axiom)          
    return list(new_axiom)

def generate_AllTurtle(cad,theta,size,moves):
    lia.setup(width=1.0,height=1.0)
    lia.tracer(0, 0)
    lia.penup()
    lia.setpos(0,0)
    lia.pendown()
    lia.setheading(90)
    for car in cad:
        if car in moves.keys():
            name_func=moves[car].__name__
            if name_func in ['right','left']:
                moves[car](theta)
            else:
                moves[car](size)
    lia.update()
    lia.done()

def generate_AllTurtle_WithMemory(cad, init_theta,theta, size, moves, pos_in, line_color, arrow_color="black", bg_color="black"):
    lia.setup(width=1.0,height=1.0)
    lia.tracer(0, 0)
    lia.color(line_color, arrow_color)
    lia.bgcolor(bg_color)
    lia.penup()
    lia.setpos(pos_in)
    lia.pendown()
    lia.setheading(init_theta)
    actual_dir=[]
    actual_heading=[]
    for car in cad:
        if car in moves.keys():
            name_func=moves[car].__name__
            if name_func in ['right','left']:
                moves[car](theta)
            else:
                moves[car](size)
        elif(car=='['):
            actual_dir.append(lia.pos())
            actual_heading.append(lia.heading())
            
            
            lia.pendown()
        elif(car==']'):
            lia.setpos(actual_dir[-1])
            lia.setheading(actual_heading[-1])
            lia.penup()
            actual_dir.pop(-1)
            actual_heading.pop(-1)
             
    lia.update()
    lia.done()


def gen_ej1():
    axiom='FX'
    prod_rules={'X' : ['X+YF'], 'Y' : ['FX-Y']}
    l = gen_cads(axiom,prod_rules, 10)
    size = 10
    ang = 90
    func_list={'F':lia.forward,'+':lia.right,'-':lia.left}
    generate_AllTurtle(l, ang, size,func_list)


def gen_ej2(sub_ej):
    axioms_list=['F','F+F+F+F', 'F+F+F+F', 'F-F-F-F','F-G-G']
    prod_list=[{'F':['F+F--F+F']},
               {'F':['F+F+F-FFF-F']},
               {'F':['FF+F+F+F+FF']},
               {'F':['F-F+F+FF-F-F+F']},
               {'F':['F-G+F+G-F'], 'G':['GG']}]
    angle_list=[60,90,90,90,120]
    functions_list=[{'F':lia.forward,'+':lia.right,'-':lia.left},
                    {'F':lia.forward,'+':lia.right,'-':lia.left},
                    {'F':lia.forward,'+':lia.right,'-':lia.left},
                    {'F':lia.forward,'+':lia.right,'-':lia.left},
                    {'F':lia.forward,'G':lia.forward,'+':lia.right,'-':lia.left}]
    all_pos_in = [(-400, -350), (-300, -100), (-350, -300), (150, -150), (350, -280)]
    all_size = [3.5, 0.36, 2.8, 0.4, 25]
    all_line_color = ["royalblue", "green", "purple", "red", "white"]
    if sub_ej<=0 and sub_ej>len(axioms_list):
        print("Ingrese un ejercicio valido...")
        return
    l = gen_cads(axioms_list[sub_ej-1],prod_list[sub_ej-1], 5)
    generate_AllTurtle_WithMemory(l,angle_list[sub_ej-1], angle_list[sub_ej-1], all_size[sub_ej-1], functions_list[sub_ej-1], all_pos_in[sub_ej-1], all_line_color[sub_ej-1])


def gen_ej3(sub_ej):
    axioms_list=['F','F','F','G','F']
    prod_list=[{'F':['F[+F]F[-F[+F][-F]]F']},
               {'F':['F[+F[+F]-F][-F]F']},
               {'F':['FF+[+F-F-F]-[-F+F+F]']},
               {'F':['FF'],'G':['FG[-F[G]-G][G+G][+F[G]+G]']},
               {'F':['F[+F]F[-F]F','F[-F]F[+F]F','F[-FF-F]F']}]
    angle_list=[29,21,22.5,22.5,29]
    functions_list=[{'F':lia.forward,'+':lia.right,'-':lia.left},
                    {'F':lia.forward,'+':lia.right,'-':lia.left},
                    {'F':lia.forward,'+':lia.right,'-':lia.left},
                    {'F':lia.forward,'G':lia.forward,'+':lia.right,'-':lia.left},
                    {'F':lia.forward,'G':lia.forward,'+':lia.right,'-':lia.left}]
    all_pos_in = [(-400, -350), (-600, -50), (-600, -100), (-390, -150), (-400, -280)]
    all_size = [3, 20, 9, 8, 5.5]
    all_line_color = ["royalblue", "green", "purple", "red", "white"]
    if sub_ej<=0 and sub_ej>len(axioms_list):
        print("Ingrese un ejercicio valido...")
        return
    l = gen_cads(axioms_list[sub_ej-1],prod_list[sub_ej-1], 5)
    generate_AllTurtle_WithMemory(l, angle_list[sub_ej-1],angle_list[sub_ej-1], all_size[sub_ej-1],functions_list[sub_ej-1], all_pos_in[sub_ej-1], all_line_color[sub_ej-1])


def move_Turtle_WithMemory(screen,turtle,cad, init_theta,theta, size, moves, pos_in, line_color, arrow_color="black"):
    turtle.color(line_color, arrow_color)
    turtle.penup()
    turtle.setpos(pos_in)
    turtle.pendown()
    turtle.setheading(init_theta)
    actual_dir=[]
    actual_heading=[]
    for car in cad:
        if car in moves.keys():
            name_func=moves[car].__name__
            if name_func in ['right','left']:
                moves[car](theta)
            else:
                moves[car](size)
        elif(car=='['):
            actual_dir.append(turtle.pos())
            actual_heading.append(turtle.heading())
            turtle.penup()
        elif(car==']'):
            turtle.setpos(actual_dir[-1])
            turtle.setheading(actual_heading[-1])
            
            turtle.pendown()
            actual_dir.pop(-1)
            actual_heading.pop(-1)

def gen_forest():
    axioms_list=['F','XGG','F','G','F']
    prod_list=[{'F':['[FD]H'],'H':['K[+FFFH[]]F'],'K':['[]FFK-H']
                ,'D':['D-F+']},
               {'F':['FF'],'G':['G[-F[G]-G][G+G][+FF[G]-G]',
                                'G[+F[G]+G][G-G][-FF[G]-G]',
                                'G[-F[G]+G][G-G][+FF[G]-G]',
                                'F[-G[F]+F][F-F][+GG[F]-F]',
                                'F[-G[F]-F][F+F][+GG[F]-F]']}]
    
    turtle=lia.Turtle()
    screen=lia.Screen()
    moves={'F':turtle.forward,'G':turtle.forward,'+':turtle.right,'-':turtle.left}
    
    leaf1 = ["F"]*30+gen_cads(axioms_list[1],prod_list[1], 5)
    leaf2 = ["F"]*30+gen_cads(axioms_list[1],prod_list[1], 5)
    leaf3 = ["F"]*30+gen_cads(axioms_list[1],prod_list[1], 5)
    leaf4 = ["F"]*30+gen_cads(axioms_list[1],prod_list[1], 5)
    leaf5 = ["F"]*30+gen_cads(axioms_list[1],prod_list[1], 5)
    
    
    screen.setup(width=1.0,height=1.0)
    screen.bgcolor('black')
    turtle._tracer(0, 0)

    move_Turtle_WithMemory(screen,turtle,leaf1,90,45,7,moves,(0,-300),"yellow")
    move_Turtle_WithMemory(screen,turtle,leaf2,90,45,7,moves,(250,-300),"yellow")
    move_Turtle_WithMemory(screen,turtle,leaf3,90,45,7,moves,(500,-300),"yellow")
    move_Turtle_WithMemory(screen,turtle,leaf4,90,45,7,moves,(-250,-300),"yellow")
    move_Turtle_WithMemory(screen,turtle,leaf5,90,45,7,moves,(-500,-300),"yellow")

    turtle._update()
    screen.mainloop()

gen_forest()