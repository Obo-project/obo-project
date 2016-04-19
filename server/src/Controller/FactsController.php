<?php
namespace App\Controller;

use Cake\Event\Event;
use App\Controller\AppController;
use Cake\Network\Exception\NotFoundException;

class FactsController extends AppController{
  public function index(){
    $this->layout = null;
    $this->loadModel('Relations');
    $this->loadModel('Entities');
    $this->autoRender = false;
    $ratio = 0.1;

    if($this->request->is(['post'])){
      $query = $this->request->data;
      $entity_query = $query['entity'];
      $relation_query = $query['relation'];
      $quantity_query = $query['quantity'];
      $comparator_query = $query['comparator'];

      $relation = $this->Relations->findByType($relation_query)->first();

      $data = $this->Entities->findByName($entity_query)->contain(['Facts'])->first();

      $print_data = "non existant";

      if($relation != null && isset($data['facts'])){
        foreach($data['facts'] as $f){
          if($f->relation_id == $relation->id) $quantity = $f->quantity;
        }
      }

      if(isset($quantity)){
        if($comparator_query == 'egal'){
          $correct = ($quantity_query - $quantity)/$quantity;
          if($correct + $ratio >= 0 && $ratio - $correct >= 0) $print_data = "yes";
          else $print_data = "no";
        }
        else if($comparator_query == 'less'){
          if($quantity <= $quantity_query) $print_data = "yes";
          else $print_data = "no";
        }
        else if($comparator_query == 'more'){
          if($quantity >= $quantity_query) $print_data = "yes";
          else $print_data = "no";
        }
      }
    }

    $this->response->type('json');
    $json = json_encode($print_data);
    $this->response->body($json . "\n");
  }
}
