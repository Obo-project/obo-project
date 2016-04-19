<?php
namespace App\Model\Table;

use Cake\ORM\Table;

class EntitiesTable extends Table{
  public function initialize(array $config){
    $this->hasMany('Facts', ['foreignKey' => 'entity_id', 'dependent' => true, 'cascadeCallbacks' => true]);
  }
}
