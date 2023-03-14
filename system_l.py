import turtle as lia
import random      
def gen_cads(axiom, product_rules, n_items):
    new_axiom=axiom
    for i in range(n_items):
        list_axiom=[]
        for car in new_axiom:
            aux=car
            if car in product_rules.keys():
                choose=random.choice(product_rules[car])
                list_axiom.extend(list(choose))
            else:    
                list_axiom.append(aux)
        new_axiom=''.join(list_axiom)          
    return new_axiom

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
def generate_turtle(cad, theta, size):
    lia.setup(width=1.0,height=1.0)
    lia.tracer(0, 0)
    lia.setpos(0,0)
    lia.setheading(90)
    new_cad=cad.replace('X','')
    new_cad=new_cad.replace('Y','')
    for i in new_cad:
        if i == 'F':
            lia.forward(size)
        elif i == '-':
            lia.left(theta)
        elif i == '+':
            lia.right(theta)
    lia.update()
    lia.done()
def generate_AllTurtle_WithMemory(cad,theta,size,moves):
    lia.setup(width=1.0,height=1.0)
    lia.tracer(0, 0)
    lia.penup()
    lia.setpos(-400,-150)
    lia.pendown()
    lia.setheading(theta)
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
            lia.penup()
        elif(car==']'):
            lia.setpos(actual_dir[-1])
            lia.setheading(actual_heading[-1])
            actual_dir.pop(-1)
            actual_heading.pop(-1)      
            lia.pendown()
    lia.update()
    lia.done()
def gen_ej1():
    axiom='FX'
    prod_rules={'X' : ['X+YF'], 'Y' : ['FX-Y']}
    l = gen_cads(axiom,prod_rules, 10)
    size = 10
    ang = 90
    func_list={'F':lia.forward,'+':lia.right,'-':lia.left}
    #print(func_list['F'].__name__)

    generate_AllTurtle(l, ang, size,func_list)
def gen_ej2(axiom,prod_rules):
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
    if sub_ej<=0 and sub_ej>len(axioms_list):
        print("Ingrese un ejercicio valido...")
        return
    l = gen_cads(axioms_list[sub_ej-1],prod_list[sub_ej-1], 5)
    #print(l)
    size = 10
    #print(func_list['F'].__name__)
    generate_AllTurtle_WithMemory(l, angle_list[sub_ej-1], size,functions_list[sub_ej-1])
def gen_ej3_p1(sub_ej):
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
    if sub_ej<=0 and sub_ej>len(axioms_list):
        print("Ingrese un ejercicio valido...")
        return
    l = gen_cads(axioms_list[sub_ej-1],prod_list[sub_ej-1], 5)
    #print(l)
    size = 10
    #print(func_list['F'].__name__)
    generate_AllTurtle_WithMemory(l, angle_list[sub_ej-1], size,functions_list[sub_ej-1])
  