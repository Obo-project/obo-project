<?php
namespace App\Controller;

use Cake\Event\Event;
use App\Controller\AppController;
use Cake\Network\Exception\NotFoundException;

class EntitiesController extends AppController{
  public function beforeFilter(Event $event){
    parent::beforeFilter($event);
  }

  public function initialize(){
    parent::initialize();
    $this->loadComponent('RequestHandler');
  }

  public function isAuthorized(){
    return true;
  }
}
